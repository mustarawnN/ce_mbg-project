"""fpdf2 ile PDF rapor üretimi.

Sorumlu: Ali
Not: Türkçe karakterler için fpdf2'ye TTF font (ör. DejaVuSans) eklenmeli: pdf.add_font(...)
"""

from __future__ import annotations

from daphniavision.schemas import AnalysisResult


def video_report(result: AnalysisResult, out_path: str) -> str:
    """Tek video raporu: deney bilgileri, BPM, atım sayısı, ritim metrikleri,
    güvenilirlik, uyarılar ve grafikler. PDF yolunu döndürür."""
    raise NotImplementedError


def series_report(series_df, stats: dict, ec50_fit: dict | None, out_path: str) -> str:
    """Deney serisi raporu: grup tablosu, % değişim, istatistik testi, doz-yanıt / EC50."""
    raise NotImplementedError
