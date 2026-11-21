"""Analiz sonuç ekranı.

Sorumlu: Vahit
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import streamlit as st

st.title("Analiz Sonucu")

result = st.session_state.get("last_result")
if result is None:
    st.info("Henüz analiz edilmiş bir video yok. Önce 'Video Yükle' sayfasını kullanın.")
    st.stop()

m = result.metrics
c1, c2, c3, c4 = st.columns(4)
c1.metric("BPM", f"{m.bpm:.1f}")
c2.metric("Atım sayısı", m.beat_count)
c3.metric("Ritim düzensizliği (CV)", f"{m.ibi_cv:.3f}")
c4.metric("Güvenilirlik", f"{m.reliability:.0%}")

for w in result.quality.warnings:
    st.warning(w)

# TODO (Vahit):
#  - İlk kare üzerinde ısı haritası katmanı + ROI sınırı
#  - ROI'yi elle düzeltme (daire/çokgen) ve "Yeniden analiz et" butonu -> pipeline.run(manual_roi=...)
#  - Plotly: filtrelenmiş sinyal + atım işaretleri, spektrum, atım aralıkları grafiği
#  - Sinyal yöntemi seçimi (mean_intensity / frame_diff / optical_flow)
