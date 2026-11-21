"""Kontrol / doz grupları karşılaştırması ve doz-yanıt.

Sorumlu: Mustafa
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import streamlit as st

st.title("Karşılaştırma ve Doz-Yanıt")

# TODO (Mustafa):
#  - Deney serisi seçimi -> db.list_experiments(series_id)
#  - stats.check_condition_mismatch() uyarıları (sıcaklık / yaş / bekleme farkı)
#  - Grup tablosu: n, ortalama BPM, SD, kontrole göre % değişim
#  - Kutu grafiği (Plotly) + stats.compare_groups() sonucu
#  - dose_response.fit_ec50() -> eğri ve EC50
#  - "PDF rapor indir" -> reporting.pdf_report.series_report
st.info("Bu sayfa henüz yazılmadı.")
