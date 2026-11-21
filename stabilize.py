"""Görüntü sabitleme: canlının kaymasını düzeltir.

Kalp bölgesi kareler boyunca aynı piksellerde kalmalı; yoksa vücut hareketi
sahte bir "kalp atışı" sinyali üretir.
Sorumlu: Ali
"""

from __future__ import annotations

import numpy as np


def estimate_shift(ref: np.ndarray, frame: np.ndarray) -> tuple[float, float]:
    """İki kare arasındaki kaymayı (dx, dy) bulur. İpucu: cv2.phaseCorrelate."""
    raise NotImplementedError


def stabilize(frames: np.ndarray, method: str = "phase") -> np.ndarray:
    """Tüm kareleri referans kareye hizalar.

    method: "phase" (hızlı, yalnızca öteleme) | "ecc" (cv2.findTransformECC, öteleme + dönme)
    Giriş/çıkış: (T, H, W) uint8
    """
    raise NotImplementedError
