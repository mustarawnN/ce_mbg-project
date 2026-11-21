"""Sonucun güvenilirlik skoru (0–1).

Site, düşük skorlu videoları "elle kontrol edin" uyarısıyla gösterir.
Sorumlu: Mustafa
"""

from __future__ import annotations

import numpy as np

from daphniavision.schemas import QualityFlags


def score(
    filtered_signal: np.ndarray,
    freqs: np.ndarray,
    power: np.ndarray,
    quality: QualityFlags,
) -> float:
    """Spektral tepe keskinliği, SNR ve video kalite bayraklarını birleştirir."""
    raise NotImplementedError
