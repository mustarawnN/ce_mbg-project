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


<img width="616" height="573" alt="image" src="https://github.com/user-attachments/assets/05561170-4d89-4248-b4f1-c83a01fb5d3b" />

daphniavision/                      ← GitHub repo kökü
│
├── daphniavision/                  ← Analiz paketi (arayüzden bağımsız)
│   ├── __init__.py
│   ├── config.py                   # Filtre bandı, FPS, eşikler gibi ortak ayarlar
│   ├── schemas.py                  # Modüller arası veri yapıları (dataclass)   [Ali]
│   ├── pipeline.py                 # Tüm adımları sırayla çalıştıran ana akış   [Ali]
│   │
│   ├── preprocessing/                                                         [Ali]
│   │   ├── video_io.py             # FFmpeg dönüşümü, video okuma, FPS/süre bilgisi
│   │   ├── quality.py              # Bulanıklık, pozlama, kadraj kaçışı kontrolü
│   │   ├── enhance.py              # CLAHE
│   │   └── stabilize.py            # ECC / phaseCorrelate ile sabitleme
│   │
│   ├── heart/                                                                 [Vahit]
│   │   ├── heatmap.py              # Piksel bazlı FFT ısı haritası
│   │   ├── roi.py                  # Otomatik ROI seçimi + elle seçim desteği
│   │   └── signal_extract.py       # Ortalama parlaklık / kare farkı / optik akış
│   │
│   ├── analysis/                                                              [Mustafa]
│   │   ├── filtering.py            # Trend kaldırma, band-pass
│   │   ├── bpm.py                  # FFT/Welch BPM, atım sayısı
│   │   ├── rhythm.py               # Atım aralığı, SD, CV, RMSSD, atlanan atım
│   │   ├── quality_score.py        # Sonucun güvenilirlik skoru
│   │   ├── stats.py                # Grup karşılaştırma, ANOVA/Kruskal
│   │   └── dose_response.py        # Doz-yanıt eğrisi ve EC50
│   │
│   ├── storage/                                                               [Ali]
│   │   ├── db.py                   # SQLite bağlantısı ve sorgular
│   │   └── models.sql              # Tablo şeması (deney, video, sonuç)
│   │
│   └── reporting/                                                             [Ali]
│       ├── plots.py                # Rapor için Matplotlib grafikleri
│       └── pdf_report.py           # fpdf2 ile PDF üretimi
│
├── app/                            ← Streamlit web arayüzü
│   ├── Home.py                     # Giriş sayfası
│   ├── pages/
│   │   ├── 1_Video_Yukle.py        # Yükleme + deney bilgisi formu             [Ali]
│   │   ├── 2_Analiz_Sonucu.py      # Isı haritası, ROI düzeltme, grafikler     [Vahit]
│   │   ├── 3_Deney_Gecmisi.py      # Eski deneyleri listeleme                  [Vahit]
│   │   └── 4_Karsilastirma.py      # Kontrol-doz, % değişim, EC50              [Mustafa]
│   └── components/                 # Ortak arayüz parçaları (grafik, kart, form)
│
├── tests/                          ← Herkes kendi modülünün testini yazar
│   ├── test_preprocessing.py
│   ├── test_heart.py
│   ├── test_analysis.py            # Sentetik sinüs sinyalleriyle BPM testi
│   └── fixtures/                   # Küçük örnek videolar ve sinyaller
│
├── data/                           ← Git'e YÜKLENMEZ (.gitignore)
│   ├── raw/                        # MBG'den gelen orijinal videolar
│   ├── processed/                  # FFmpeg ile dönüştürülmüş videolar
│   ├── ground_truth/               # Elle sayılan atımlar (CSV)
│   └── daphniavision.db            # SQLite veritabanı
│
├── notebooks/                      # Deneme ve keşif çalışmaları (Jupyter)
├── scripts/
│   ├── batch_analyze.py            # Klasördeki tüm videoları toplu analiz
│   └── validate.py                 # Elle sayım ile karşılaştırma (Pearson r)
├── docs/                           # Mimari şeması, haftalık raporlar, ödevler
│
├── requirements.txt                # Kütüphane listesi ve sürümleri
├── .gitignore
├── Dockerfile                      # İsteğe bağlı
└── README.md                       # Kurulum ve çalıştırma talimatı
