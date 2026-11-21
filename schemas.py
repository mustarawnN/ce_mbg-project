"""Modüller arası veri yapıları (arayüz sözleşmesi).

Akış:
    Ali (preprocessing)  -> PreprocessedVideo
    Vahit (heart)        -> HeartSignal
    Mustafa (analysis)   -> HeartMetrics
    pipeline             -> AnalysisResult  -> site / veritabanı / PDF

Bu dosyadaki alanları değiştirmeden önce ekiple konuşun: herkesin kodu buna bağlı.
Sorumlu: Ali
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

import numpy as np


@dataclass
class ExperimentMeta:
    """Video yüklenirken formdan girilen deney bilgileri."""

    substance: str                          # "kontrol", "kafein", "etanol", ...
    dose: float                             # kontrol için 0
    dose_unit: str = "mg/L"
    is_control: bool = False
    temperature_c: float | None = None      # su sıcaklığı
    age_hours: float | None = None          # canlının yaşı
    body_length_mm: float | None = None     # canlının boyu
    immobilization: str = "pamuk"           # sabitleme yöntemi
    acclimation_min: float | None = None    # sabitlendikten sonra bekleme süresi
    exposure_min: float | None = None       # maddeye maruz kalma süresi
    magnification: str | None = None        # ör. "10x"
    series_id: str | None = None            # aynı deney serisindeki videoları gruplar
    notes: str = ""


@dataclass
class QualityFlags:
    """Videonun kalite kontrol sonucu."""

    blur_score: float | None = None                     # yüksek = daha net
    exposure_ok: bool = True
    out_of_frame_segments: list[tuple[float, float]] = field(default_factory=list)  # (başlangıç_s, bitiş_s)
    warnings: list[str] = field(default_factory=list)


@dataclass
class PreprocessedVideo:
    """Ali -> Vahit"""

    frames: np.ndarray          # (T, H, W) uint8, gri tonlu, sabitlenmiş
    fps: float                  # SABİT kare hızı
    duration_s: float
    resolution: tuple[int, int] # (genişlik, yükseklik)
    quality: QualityFlags
    source_path: str


@dataclass
class HeartSignal:
    """Vahit -> Mustafa"""

    signal: np.ndarray          # (T,) ham kalp sinyali
    fps: float
    roi_mask: np.ndarray        # (H, W) bool, kalp bölgesi
    heatmap: np.ndarray         # (H, W) float, kalp frekans bandındaki enerji
    method: str                 # "mean_intensity" | "frame_diff" | "optical_flow"
    roi_auto: bool = True       # False: ROI elle seçildi


@dataclass
class HeartMetrics:
    """Mustafa -> site / veritabanı / rapor"""

    bpm: float                          # spektrumdan ortalama kalp hızı
    beat_count: int                     # kayıt boyunca sayılan atım
    duration_s: float
    beat_times_s: np.ndarray            # her atımın zamanı (s)
    ibi_s: np.ndarray                   # atımlar arası süreler (s)
    ibi_mean_s: float
    ibi_sd_s: float
    ibi_cv: float                       # değişkenlik katsayısı (ritim düzensizliği)
    rmssd_s: float
    pauses: int                         # duraksama / atlanan atım sayısı
    reliability: float                  # 0–1 arası güvenilirlik skoru
    filtered_signal: np.ndarray
    spectrum_freqs_hz: np.ndarray
    spectrum_power: np.ndarray


@dataclass
class AnalysisResult:
    """Tek bir videonun tüm analiz sonucu."""

    meta: ExperimentMeta
    source_path: str
    fps: float
    quality: QualityFlags
    heart: HeartSignal
    metrics: HeartMetrics
    created_at: datetime = field(default_factory=datetime.now)
