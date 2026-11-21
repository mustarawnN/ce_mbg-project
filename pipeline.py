"""Tüm analiz adımlarını sırayla çalıştıran ana akış.

Site, toplu analiz betiği ve testler yalnızca `run()` fonksiyonunu çağırır.
Sorumlu: Ali
"""

from __future__ import annotations

from collections.abc import Callable

import numpy as np

from daphniavision.analysis import bpm, filtering, quality_score, rhythm
from daphniavision.heart import heatmap, roi, signal_extract
from daphniavision.preprocessing import enhance, quality, stabilize, video_io
from daphniavision.schemas import AnalysisResult, ExperimentMeta, HeartMetrics, PreprocessedVideo

ProgressFn = Callable[[float, str], None]


def preprocess(video_path: str, progress: ProgressFn | None = None) -> PreprocessedVideo:
    """Ali'nin modülü: dönüştür -> oku -> kalite kontrol -> kontrast -> sabitle."""
    _p = progress or (lambda *_: None)

    _p(0.05, "Video standartlaştırılıyor")
    std_path = video_io.normalize_video(video_path)

    _p(0.15, "Kareler okunuyor")
    frames, fps = video_io.read_frames(std_path)

    _p(0.25, "Kalite kontrol")
    flags = quality.check_quality(frames, fps)

    _p(0.35, "Kontrast artırılıyor")
    frames = enhance.apply_clahe(frames)

    _p(0.45, "Görüntü sabitleniyor")
    frames = stabilize.stabilize(frames)

    h, w = frames.shape[1:3]
    return PreprocessedVideo(
        frames=frames,
        fps=fps,
        duration_s=len(frames) / fps,
        resolution=(w, h),
        quality=flags,
        source_path=video_path,
    )


def run(
    video_path: str,
    meta: ExperimentMeta,
    manual_roi: np.ndarray | None = None,
    method: str | None = None,
    progress: ProgressFn | None = None,
) -> AnalysisResult:
    """Bir videoyu baştan sona analiz eder.

    manual_roi: kullanıcı sitede kalbi elle işaretlediyse (H, W) bool maske.
    method: None ise en iyi sinyal yöntemi otomatik seçilir.
    """
    _p = progress or (lambda *_: None)

    video = preprocess(video_path, progress)

    # --- Vahit'in modülü ---
    _p(0.60, "Kalp bölgesi bulunuyor")
    hmap = heatmap.compute_heatmap(video.frames, video.fps)
    if manual_roi is not None:
        roi_mask, roi_auto = manual_roi, False
    else:
        roi_mask, roi_auto = roi.select_roi(hmap), True

    _p(0.70, "Kalp sinyali çıkarılıyor")
    heart = signal_extract.extract_best_signal(
        video.frames, video.fps, roi_mask, hmap, method=method, roi_auto=roi_auto
    )

    # --- Mustafa'nın modülü ---
    _p(0.85, "BPM ve ritim hesaplanıyor")
    filtered = filtering.bandpass(filtering.detrend(heart.signal), heart.fps)
    freqs, power = bpm.spectrum(filtered, heart.fps)
    bpm_value = bpm.bpm_from_spectrum(freqs, power)
    beat_times = bpm.detect_beats(filtered, heart.fps, bpm_value)
    rhythm_m = rhythm.rhythm_metrics(beat_times)
    reliability = quality_score.score(filtered, freqs, power, video.quality)

    metrics = HeartMetrics(
        bpm=bpm_value,
        beat_count=len(beat_times),
        duration_s=video.duration_s,
        beat_times_s=beat_times,
        filtered_signal=filtered,
        spectrum_freqs_hz=freqs,
        spectrum_power=power,
        reliability=reliability,
        **rhythm_m,
    )

    _p(1.0, "Tamamlandı")
    return AnalysisResult(
        meta=meta,
        source_path=video_path,
        fps=video.fps,
        quality=video.quality,
        heart=heart,
        metrics=metrics,
    )
