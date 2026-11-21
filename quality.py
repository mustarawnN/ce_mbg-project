"""Video kalite kontrolü.

Sorumlu: Ali
"""

from __future__ import annotations

import numpy as np

from daphniavision.schemas import QualityFlags


def blur_score(frame: np.ndarray) -> float:
    """Netlik skoru. İpucu: Laplacian varyansı (cv2.Laplacian(...).var())."""
    raise NotImplementedError


def check_exposure(frames: np.ndarray) -> bool:
    """Aşırı karanlık / aşırı parlak (doymuş piksel oranı) kontrolü."""
    raise NotImplementedError


def detect_out_of_frame(frames: np.ndarray, fps: float) -> list[tuple[float, float]]:
    """Canlının kaydığı / zıpladığı zaman aralıklarını bulur (büyük kare farkları)."""
    raise NotImplementedError


def check_quality(frames: np.ndarray, fps: float) -> QualityFlags:
    """Tüm kontrolleri çalıştırır, FPS ve süre için config'deki eşiklere göre uyarı ekler."""
    raise NotImplementedError
