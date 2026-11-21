"""Kontrast iyileştirme.

Sorumlu: Ali
"""

from __future__ import annotations

import numpy as np


def apply_clahe(frames: np.ndarray) -> np.ndarray:
    """Her kareye CLAHE uygular (config.CLAHE_CLIP_LIMIT, config.CLAHE_TILE_GRID).

    Giriş/çıkış: (T, H, W) uint8
    """
    raise NotImplementedError
