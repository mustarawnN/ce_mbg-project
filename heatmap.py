"""Kalp ısı haritası: her pikselin kalp frekans bandındaki enerjisi.

Fikir: Her pikselin zaman içindeki parlaklığına FFT uygulanır. Kalp bandında
(config.HEART_BAND_HZ) en çok enerji taşıyan bölge kalptir. Bağırsak hareketi
daha yavaş, bacak çırpması farklı frekansta olduğu için ayrışır.
Sorumlu: Vahit
"""

from __future__ import annotations

import numpy as np


def compute_heatmap(
    frames: np.ndarray,
    fps: float,
    band_hz: tuple[float, float] | None = None,
    downscale: int = 2,
) -> np.ndarray:
    """(T, H, W) karelerden (H, W) ısı haritası üretir.

    downscale: hız için kareler önce küçültülür, sonuç orijinal boyuta büyütülür.
    İpucu: np.fft.rfft(frames, axis=0) ve np.fft.rfftfreq(T, 1/fps).
    Dönüş 0–1 arasına normalize edilmiş olmalı.
    """
    raise NotImplementedError


def dominant_frequency_map(frames: np.ndarray, fps: float) -> np.ndarray:
    """(İsteğe bağlı) Her pikselin baskın frekansı. Hata ayıklama ve görselleştirme için."""
    raise NotImplementedError
