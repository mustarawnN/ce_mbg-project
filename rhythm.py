"""Ritim düzeni metrikleri.

Sorumlu: Mustafa
"""

from __future__ import annotations

import numpy as np


def rhythm_metrics(beat_times_s: np.ndarray) -> dict:
    """Atım zamanlarından ritim metriklerini hesaplar.

    Dönüş anahtarları schemas.HeartMetrics alanlarıyla AYNI olmalı:
        ibi_s       : atımlar arası süreler (np.ndarray)
        ibi_mean_s  : ortalama aralık
        ibi_sd_s    : standart sapma
        ibi_cv      : sd / ortalama (ritim düzensizliği)
        rmssd_s     : ardışık farkların karesel ortalamasının kökü
        pauses      : ortalamanın config.PAUSE_FACTOR katından uzun aralık sayısı
    """
    raise NotImplementedError
