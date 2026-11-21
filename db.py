"""SQLite veritabanı işlemleri.

Sorumlu: Ali
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd

from daphniavision import config
from daphniavision.schemas import AnalysisResult, ExperimentMeta

SCHEMA_PATH = Path(__file__).with_name("models.sql")


def connect(db_path: Path | str | None = None) -> sqlite3.Connection:
    path = Path(db_path or config.DB_PATH)
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db(db_path: Path | str | None = None) -> None:
    """Tabloları oluşturur (varsa dokunmaz)."""
    with connect(db_path) as conn:
        conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))


def insert_video(conn: sqlite3.Connection, file_path: str, meta: ExperimentMeta,
                 fps: float | None = None, duration_s: float | None = None) -> int:
    """Videoyu ve deney bilgisini kaydeder, video_id döndürür."""
    raise NotImplementedError


def insert_result(conn: sqlite3.Connection, video_id: int, result: AnalysisResult) -> int:
    """Analiz sonucunu kaydeder. Diziler (sinyal, spektrum, atım zamanları) .npz olarak
    data/processed/ altına yazılır, yolu arrays_path sütununa konur."""
    raise NotImplementedError


def list_experiments(conn: sqlite3.Connection, series_id: str | None = None) -> pd.DataFrame:
    """videos + results birleşik tablosu (deney geçmişi ve karşılaştırma sayfaları için)."""
    raise NotImplementedError


def get_result(conn: sqlite3.Connection, result_id: int) -> dict:
    """Tek bir sonucu dizileriyle birlikte yükler."""
    raise NotImplementedError
