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

Kişi	Modül	Görevler	Zorluk
Ali	Ön işleme ve video hattı	FFmpeg ile sabit FPS ve tek formata dönüştürme. Video bilgilerini okuma (FPS, süre, çözünürlük). Kalite kontrol: bulanıklık, aşırı karanlık/parlaklık, canlının kadrajdan kaçtığı bölümleri işaretleme. CLAHE ile kontrast artırma. Görüntü sabitleme (ECC / phaseCorrelate).	Orta-Zor
Vahit	Kalbin bulunması ve sinyal çıkarma	Piksel bazlı FFT ile kalp ısı haritası. Kalp bölgesinin (ROI) otomatik seçimi, başarısız olursa elle seçime geçiş. Üç sinyal yöntemi: ROI ortalama parlaklık, kareler arası fark, optik akış. En temiz sinyali veren yöntemin seçimi.	Zor
Mustafa	Sinyal analizi ve metrikler	Trend kaldırma ve band-pass filtre. FFT/Welch ile BPM. find_peaks ile atım sayısı. Ritim metrikleri: atımlar arası süre, değişkenlik (SD, CV, RMSSD), atlanan atım ve duraksamalar. Her sonuç için güvenilirlik skoru.	Orta-Zor
Web Sitesi
 
Kişi	Modül	Görevler	Zorluk
Ali	Yükleme, veritabanı, rapor	Video yükleme sayfası ve deney bilgisi formu (madde, doz, sıcaklık, yaş/boy, pamuk, bekleme süresi). SQLite şeması ve kayıt işlemleri. Analiz hattının siteden çalıştırılması (ilerleme çubuğu). PDF rapor.	Orta
Vahit	Analiz sonuç ekranı	Videoda kalp ısı haritası katmanı ve ROI önizlemesi. ROI'yi elle düzeltme ve yeniden analiz. Sinyal ve spektrum grafikleri (Plotly), atımların sinyal üzerinde işaretlenmesi. Deney geçmişi sayfası.	Orta
Mustafa	Karşılaştırma ve doz-yanıt	Kontrol ve doz gruplarının karşılaştırılması, "kontrole göre % değişim". İstatistik testi (ANOVA veya Kruskal-Wallis). Doz-yanıt eğrisi ve EC50. Koşulları farklı videolar karışırsa (sıcaklık, yaş) uyarı verme.
