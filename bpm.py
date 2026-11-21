"""BPM ve atım tespiti.

Sorumlu: Mustafa
"""

from __future__ import annotations

import numpy as np


def spectrum(signal: np.ndarray, fps: float) -> tuple[np.ndarray, np.ndarray]:
    """Güç spektrumu. İpucu: scipy.signal.welch. Dönüş: (frekanslar_hz, güç)"""
    raise NotImplementedError


def bpm_from_spectrum(freqs: np.ndarray, power: np.ndarray, band_hz: tuple[float, float] | None = None) -> float:
    """Kalp bandındaki en güçlü tepenin frekansı x 60."""
    raise NotImplementedError


def detect_beats(signal: np.ndarray, fps: float, expected_bpm: float | None = None) -> np.ndarray:
    """Her atımın zamanını (s) bulur.

    İpucu: scipy.signal.find_peaks; expected_bpm'den en kısa tepe aralığını
    (distance) hesaplayın, prominence ile küçük gürültü tepelerini eleyin.
    """
    raise NotImplementedError
