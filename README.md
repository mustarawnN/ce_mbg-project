# DaphniaVision

*Daphnia magna* mikroskop videolarından **kalp atım hızı (BPM), atım sayısı ve ritim düzenini** otomatik ölçen; toksik madde dozlarının kalp üzerindeki etkisini kontrol grubuyla karşılaştıran web tabanlı karar destek platformu.

Disiplinlerarası Tasarım Projesi — Takım 19

## Kurulum

```bash
git clone <repo-adresi>
cd daphniavision
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

FFmpeg ayrıca kurulmalı: `winget install ffmpeg` (Windows), `brew install ffmpeg` (macOS), `sudo apt install ffmpeg` (Ubuntu).

## Çalıştırma

```bash
streamlit run app/Home.py                                   # web paneli
pytest                                                      # testler
python scripts/batch_analyze.py data/raw                    # toplu analiz
python scripts/validate.py data/processed/sonuclar.csv data/ground_truth/elle_sayim.csv
```

## Analiz Akışı

```
Video ─► [Ali] ön işleme ─► [Vahit] kalp tespiti ─► [Mustafa] sinyal analizi ─► Site / DB / PDF
          FFmpeg (sabit FPS)    FFT ısı haritası        band-pass filtre
          kalite kontrol        ROI (oto / elle)        BPM, atım sayısı
          CLAHE, sabitleme      sinyal çıkarma          ritim (CV, RMSSD, duraksama)
```

Modüller arası veri yapıları `daphniavision/schemas.py` dosyasında tanımlıdır. **Bu dosyayı değiştirmeden önce ekiple konuşun.**

## Görev Dağılımı

| Kişi | Görüntü işleme | Web |
|---|---|---|
| **Ali** (Sistem ve Mimari) | `preprocessing/`, `pipeline.py`, `schemas.py` | `1_Video_Yukle.py`, `storage/`, `reporting/`, entegrasyon |
| **Vahit** (Görüntü İşleme) | `heart/` | `2_Analiz_Sonucu.py`, `3_Deney_Gecmisi.py` |
| **Mustafa** (Algoritma ve Analitik) | `analysis/` (filtre, BPM, ritim) | `4_Karsilastirma.py`, `analysis/stats.py`, `analysis/dose_response.py` |

## Kurallar

- `app/` içinde analiz kodu yazılmaz; sayfalar yalnızca `daphniavision` paketini çağırır.
- Videolar Git'e yüklenmez (`data/` klasörü `.gitignore`'da). Ortak Drive klasörü kullanılır.
- Her modül kendi dalında (branch) geliştirilir: `feature/preprocessing`, `feature/heart`, `feature/analysis` ...
- Her fonksiyon için `tests/` altında test yazılır. Henüz yazılmamış fonksiyonların testleri **atlanır (skip)**, başarısız sayılmaz.
- Sabit sayılar (filtre bandı, eşikler) `config.py` içinde tutulur.

## Çekim Standardı (MBG ekibi için)

- En az **30 FPS** (tercihen 60), sabit kare hızı
- **20 saniye** kayıt
- Otomatik pozlama ve otomatik odak **kapalı**, sabit ışık
- Canlı yan (lateral) pozisyonda, kalp kadrajın ortasında
- Her video için deney bilgileri: madde, doz, sıcaklık, yaş/boy, sabitleme sonrası bekleme süresi
