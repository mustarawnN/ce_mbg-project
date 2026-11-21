## Kullanılan Teknolojiler

### Görüntü ve Sinyal İşleme

| Teknoloji | Kullanım | Neden |
| :--- | :--- | :--- |
| **Python** | Ana dil | Görüntü işleme, sinyal işleme ve web tek dilde yazılır. |
| **FFmpeg** | Videoyu sabit FPS'e ve tek formata çevirme | Telefon/mikroskop videoları değişken kare hızlı olabilir. FFT ancak sabit FPS ile doğru BPM verir. |
| **OpenCV** | Video okuma, CLAHE, görüntü sabitleme (`ECC` / `phaseCorrelate`), optik akış (`Farneback`), kontur | Düşük kontrastı artırır, canlının kaymasını düzeltir, kalp duvarının hareketini ölçer. Hızlı olduğu için 60 saniye kriterini karşılar. |
| **NumPy** | Piksel bazlı hesaplar | Her pikselin zaman sinyali ve ROI ortalaması vektörel olarak hızlıca hesaplanır. |
| **SciPy** (`signal`, `fft`, `stats`, `optimize`) | Filtre, FFT/Welch, tepe bulma, korelasyon, EC50 | Butterworth band-pass gürültüyü ve bağırsak hareketini ayırır. FFT ısı haritası kalbi otomatik bulur. `find_peaks` atımları ve aritmiyi verir. Pearson `r` kriter 3'ü ölçer. `curve_fit` doz-yanıt eğrisinden EC50'yi bulur. |
| **scikit-image** | Kalp segmentasyonu *(isteğe bağlı)* | Kasılma oranı için kalp alanı ölçülecekse aktif kontur ve morfoloji araçları gerekir. |
| **pandas** | Sonuç tabloları | Video, doz ve BPM kayıtlarını düzenler, CSV olarak dışa aktarır. |
| **Matplotlib** | Rapor grafikleri | Isı haritası, filtrelenmiş sinyal, spektrum ve doz-yanıt eğrisi PDF'e konur. |

### Web Paneli

| Teknoloji | Kullanım | Neden |
| :--- | :--- | :--- |
| **Streamlit** | Arayüz | Video yükleme, ROI önizleme, sonuç grafikleri ve indirme butonu sadece Python ile yapılır. 11. hafta hedefi için en hızlı yol budur. |
| **Plotly** | Etkileşimli grafikler | Araştırmacı sinyale yakınlaşıp tek tek atımları inceleyebilir. |
| **fpdf2** | Otomatik PDF rapor | Tek tıkla BPM, aritmi ve EC50 raporu üretir (kriter 5). |
| **SQLite** | Deney kayıtları | Kurulum gerektirmez. Doz, video ve sonuçlar saklanır, eski deneyler tekrar açılabilir. |


GÖREV DAĞILIMLARI

<img width="757" height="685" alt="image" src="https://github.com/user-attachments/assets/17f07790-fd2c-4efe-b48b-350f6c989adb" />



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
