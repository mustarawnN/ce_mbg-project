"""Grup karşılaştırmaları.

Sorumlu: Mustafa
"""

from __future__ import annotations

import pandas as pd


def percent_change_vs_control(df: pd.DataFrame, value_col: str = "bpm") -> pd.DataFrame:
    """Her doz grubunun kontrole göre % değişimi.

    df sütunları: substance, dose, is_control, <value_col>, ...
    Dönüş: dose, n, mean, sd, pct_change
    """
    raise NotImplementedError


def compare_groups(df: pd.DataFrame, value_col: str = "bpm") -> dict:
    """Gruplar arası fark testi. Normal dağılım varsa ANOVA, yoksa Kruskal-Wallis.

    Dönüş: {"test": "anova" | "kruskal", "statistic": float, "p_value": float}
    """
    raise NotImplementedError


def check_condition_mismatch(df: pd.DataFrame, temp_tol_c: float = 1.0) -> list[str]:
    """Aynı seride sıcaklık / yaş / bekleme süresi farklı videolar varsa uyarı listesi döndürür."""
    raise NotImplementedError
