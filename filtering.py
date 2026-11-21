"""Sinyal filtreleme.

Sorumlu: Mustafa
"""

from __future__ import annotations

import numpy as np


def detrend(signal: np.ndarray) -> np.ndarray:
    """Yavaş parlaklık kaymasını kaldırır. İpucu: scipy.signal.detrend."""
    raise NotImplementedError


def bandpass(
    signal: np.ndarray,
    fps: float,
    band_hz: tuple[float, float] | None = None,
    order: int | None = None,
) -> np.ndarray:
    """Butterworth band-pass (config.HEART_BAND_HZ). Faz kaymasız: scipy.signal.filtfilt veya sosfiltfilt."""
    raise NotImplementedError
