"""DaphniaVision ana sayfası.

Çalıştırma (repo kökünden):  streamlit run app/Home.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st

from daphniavision.storage import db

st.set_page_config(page_title="DaphniaVision", page_icon="🔬", layout="wide")

db.init_db()

st.title("DaphniaVision")
st.subheader("Daphnia magna kalp atım analizi ve nörotoksisite karar destek platformu")

st.markdown(
    """
**Nasıl kullanılır?**

1. **Video Yükle:** Mikroskop videosunu yükleyin ve deney bilgilerini girin.
2. **Analiz Sonucu:** Kalp bölgesini kontrol edin; BPM, atım sayısı ve ritim düzenini inceleyin.
3. **Deney Geçmişi:** Önceki analizleri görüntüleyin.
4. **Karşılaştırma:** Kontrol ve doz gruplarını karşılaştırın, EC50 hesaplayın, PDF rapor alın.
"""
)
