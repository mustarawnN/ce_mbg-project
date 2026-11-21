"""Video yükleme ve deney bilgisi formu.

Sorumlu: Ali
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import streamlit as st

from daphniavision import config
from daphniavision.schemas import ExperimentMeta

st.title("Video Yükle")

uploaded = st.file_uploader("Mikroskop videosu", type=["mp4", "mov", "avi", "mkv"])

with st.form("meta_form"):
    st.subheader("Deney bilgileri")
    c1, c2, c3 = st.columns(3)
    with c1:
        series_id = st.text_input("Deney serisi", placeholder="ör. kafein-seri-1")
        is_control = st.checkbox("Kontrol grubu (madde yok)")
        substance = st.text_input("Madde", value="kontrol" if is_control else "kafein")
        dose = st.number_input("Doz", min_value=0.0, value=0.0, step=0.1)
        dose_unit = st.selectbox("Birim", ["mg/L", "µg/L", "%"])
    with c2:
        temperature_c = st.number_input("Su sıcaklığı (°C)", value=20.0, step=0.5)
        age_hours = st.number_input("Canlının yaşı (saat)", min_value=0.0, value=24.0)
        body_length_mm = st.number_input("Canlının boyu (mm)", min_value=0.0, value=0.0, step=0.1)
        magnification = st.text_input("Büyütme", value="10x")
    with c3:
        immobilization = st.selectbox("Sabitleme", ["pamuk", "yok", "diğer"])
        acclimation_min = st.number_input("Sabitleme sonrası bekleme (dk)", min_value=0.0, value=5.0)
        exposure_min = st.number_input("Maddeye maruz kalma süresi (dk)", min_value=0.0, value=0.0)
    notes = st.text_area("Notlar")
    submitted = st.form_submit_button("Kaydet ve analiz et")

if submitted:
    if uploaded is None:
        st.error("Lütfen önce bir video yükleyin.")
        st.stop()

    meta = ExperimentMeta(
        substance=substance, dose=0.0 if is_control else dose, dose_unit=dose_unit,
        is_control=is_control, temperature_c=temperature_c, age_hours=age_hours,
        body_length_mm=body_length_mm or None, immobilization=immobilization,
        acclimation_min=acclimation_min, exposure_min=exposure_min,
        magnification=magnification, series_id=series_id or None, notes=notes,
    )

    config.RAW_DIR.mkdir(parents=True, exist_ok=True)
    video_path = config.RAW_DIR / uploaded.name
    video_path.write_bytes(uploaded.getbuffer())

    # TODO (Ali): db.insert_video -> pipeline.run(progress=...) -> db.insert_result
    #             sonucu st.session_state["last_result"] içine koyup Analiz Sonucu sayfasına yönlendir.
    bar = st.progress(0.0, text="Analiz başlıyor")
    try:
        from daphniavision import pipeline

        result = pipeline.run(str(video_path), meta, progress=lambda p, t: bar.progress(p, text=t))
        st.session_state["last_result"] = result
        st.success("Analiz tamamlandı. 'Analiz Sonucu' sayfasına geçin.")
    except NotImplementedError:
        st.warning("Analiz modülleri henüz yazılmadı (NotImplementedError).")
