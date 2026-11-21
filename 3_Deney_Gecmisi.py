"""Deney geçmişi.

Sorumlu: Vahit
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import streamlit as st

st.title("Deney Geçmişi")

# TODO (Vahit):
#  - db.list_experiments() tablosu; seri / madde / tarih filtreleri
#  - Satıra tıklayınca db.get_result() ile sonucu açıp Analiz Sonucu sayfasında göster
#  - CSV olarak dışa aktarma (st.download_button)
st.info("Bu sayfa henüz yazılmadı.")
