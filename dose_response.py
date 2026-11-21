"""Doz-yanıt eğrisi ve EC50.

Sorumlu: Mustafa
"""

from __future__ import annotations

import numpy as np


def four_param_logistic(dose: np.ndarray, bottom: float, top: float, ec50: float, hill: float) -> np.ndarray:
    """4 parametreli lojistik (Hill) modeli."""
    raise NotImplementedError


def fit_ec50(doses: np.ndarray, responses: np.ndarray) -> dict:
    """Modeli scipy.optimize.curve_fit ile oturtur.

    responses: kontrole göre normalize edilmiş yanıt (ör. % BPM değişimi).
    Dönüş: {"ec50": float, "ec50_ci": (alt, üst), "bottom": ..., "top": ..., "hill": ..., "r2": float}
    """
    raise NotImplementedError
