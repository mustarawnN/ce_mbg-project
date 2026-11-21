"""Kalp bölgesinin (ROI) seçimi.

Sorumlu: Vahit
"""

from __future__ import annotations

import numpy as np


def select_roi(heatmap: np.ndarray, percentile: float = 95.0) -> np.ndarray:
    """Isı haritasından kalp maskesini otomatik çıkarır.

    Adımlar: eşikleme (percentile) -> morfolojik temizlik -> en büyük bağlı bileşen.
    Dönüş: (H, W) bool maske
    """
    raise NotImplementedError


def roi_from_points(shape: tuple[int, int], points: list[tuple[int, int]]) -> np.ndarray:
    """Kullanıcının sitede çizdiği çokgenden (x, y noktaları) maske üretir.

    İpucu: cv2.fillPoly
    """
    raise NotImplementedError


def roi_from_circle(shape: tuple[int, int], center: tuple[int, int], radius: int) -> np.ndarray:
    """Basit elle seçim: merkez + yarıçap ile dairesel maske."""
    raise NotImplementedError
