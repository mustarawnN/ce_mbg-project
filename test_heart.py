"""Kalp tespiti ve sinyal çıkarma testleri. Sorumlu: Vahit"""

import numpy as np

from conftest import not_implemented_skip
from daphniavision.heart import heatmap, roi, signal_extract


def test_heatmap_peaks_at_heart(heart_video):
    frames, fps, (cx, cy, r) = heart_video
    hmap = not_implemented_skip(heatmap.compute_heatmap, frames, fps)
    assert hmap.shape == frames.shape[1:]
    y, x = np.unravel_index(np.argmax(hmap), hmap.shape)
    # en sıcak nokta dairenin sınırına yakın olmalı (kasılma kenarda görünür)
    assert abs(np.hypot(x - cx, y - cy) - r) < r * 0.6


def test_auto_roi_covers_heart(heart_video):
    frames, fps, (cx, cy, r) = heart_video
    hmap = not_implemented_skip(heatmap.compute_heatmap, frames, fps)
    mask = not_implemented_skip(roi.select_roi, hmap)
    assert mask.dtype == bool
    assert mask[cy - r: cy + r, cx - r: cx + r].sum() > 0.5 * mask.sum()


def test_mean_intensity_length(heart_video):
    frames, _, (cx, cy, r) = heart_video
    mask = np.zeros(frames.shape[1:], dtype=bool)
    mask[cy - r: cy + r, cx - r: cx + r] = True
    sig = not_implemented_skip(signal_extract.mean_intensity, frames, mask)
    assert sig.shape == (len(frames),)
