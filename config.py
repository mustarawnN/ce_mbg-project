"""Projenin ortak ayarları. Sabit sayıları kodun içine gömmek yerine buraya yazın."""

from pathlib import Path

# --- Klasörler ---
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
GROUND_TRUTH_DIR = DATA_DIR / "ground_truth"
DB_PATH = DATA_DIR / "daphniavision.db"

# --- Video ---
TARGET_FPS: float | None = None   # None: orijinal FPS korunur ama sabit FPS'e çevrilir
MIN_FPS = 30.0                    # Bunun altındaki videolar için uyarı verilir
MIN_DURATION_S = 10.0             # Güvenilir BPM için en kısa kayıt süresi

# --- Kalp sinyali ---
HEART_BAND_HZ = (1.5, 8.0)        # 90–480 BPM; MBG'den gelecek kontrol verisine göre daraltılacak
FILTER_ORDER = 4                  # Butterworth filtre derecesi

# --- Ön işleme ---
CLAHE_CLIP_LIMIT = 2.0
CLAHE_TILE_GRID = (8, 8)

# --- Ritim analizi ---
PAUSE_FACTOR = 1.8                # Atım aralığı ortalamanın bu katından uzunsa "duraksama" sayılır
