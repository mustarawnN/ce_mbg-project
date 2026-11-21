"""PDF rapor için Matplotlib grafikleri. Her fonksiyon matplotlib Figure döndürür.

Sorumlu: Ali
"""

from __future__ import annotations

from daphniavision.schemas import AnalysisResult


def plot_heatmap_overlay(result: AnalysisResult, first_frame=None):
    """İlk kare üzerinde kalp ısı haritası ve ROI sınırı."""
    raise NotImplementedError


def plot_signal(result: AnalysisResult):
    """Filtrelenmiş sinyal ve tespit edilen atımlar."""
    raise NotImplementedError


def plot_spectrum(result: AnalysisResult):
    """Güç spektrumu, BPM tepesi işaretli."""
    raise NotImplementedError


def plot_ibi(result: AnalysisResult):
    """Atımlar arası süreler (ritim düzeni)."""
    raise NotImplementedError


def plot_dose_response(doses, responses, fit: dict):
    """Doz-yanıt noktaları, oturtulan eğri ve EC50."""
    raise NotImplementedError
