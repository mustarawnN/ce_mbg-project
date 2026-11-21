"""Ön işleme testleri. Sorumlu: Ali"""

import numpy as np

from conftest import not_implemented_skip
from daphniavision.preprocessing import enhance, quality, stabilize


def test_clahe_keeps_shape_and_dtype(heart_video):
    frames, _, _ = heart_video
    out = not_implemented_skip(enhance.apply_clahe, frames)
    assert out.shape == frames.shape
    assert out.dtype == np.uint8


def test_stabilize_removes_shift(heart_video):
    frames, _, _ = heart_video
    shifted = frames.copy()
    shifted[len(frames) // 2:] = np.roll(frames[len(frames) // 2:], shift=5, axis=2)  # yarısını 5 px kaydır
    out = not_implemented_skip(stabilize.stabilize, shifted)
    diff_before = np.abs(shifted[-1].astype(float) - shifted[0]).mean()
    diff_after = np.abs(out[-1].astype(float) - out[0]).mean()
    assert diff_after < diff_before


def test_quality_flags_low_fps():
    frames = np.full((100, 64, 64), 128, dtype=np.uint8)
    flags = not_implemented_skip(quality.check_quality, frames, 15.0)
    assert any("FPS" in w or "fps" in w for w in flags.warnings)
