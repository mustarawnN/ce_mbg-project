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

