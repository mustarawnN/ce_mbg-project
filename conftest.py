"""Testlerde ortak kullanılan sentetik veriler.

Gerçek video beklemeden çalışabilmek için bilinen frekanslı sinyaller ve
yapay "kalp" videosu üretilir.
"""

import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def make_heart_signal(bpm: float = 240.0, fps: float = 30.0, duration_s: float = 20.0,
                      noise: float = 0.2, seed: int = 0) -> tuple[np.ndarray, float]:
    """Bilinen BPM'li sinüs + gürültü + yavaş kayma."""
    rng = np.random.default_rng(seed)
    t = np.arange(int(fps * duration_s)) / fps
    sig = np.sin(2 * np.pi * (bpm / 60.0) * t) + 0.5 * t / duration_s + noise * rng.standard_normal(t.size)
    return sig, fps


def make_heart_video(bpm: float = 240.0, fps: float = 30.0, duration_s: float = 10.0,
                     size: int = 128, seed: int = 0) -> tuple[np.ndarray, float, tuple[int, int, int]]:
    """Ortasında kasılıp gevşeyen bir daire olan yapay gri video.

    Dönüş: (frames (T, H, W) uint8, fps, (cx, cy, r))
    """
    rng = np.random.default_rng(seed)
    n = int(fps * duration_s)
    yy, xx = np.mgrid[:size, :size]
    cx, cy, r0 = size // 2, size // 2, size // 6
    frames = np.empty((n, size, size), dtype=np.uint8)
    for i in range(n):
        r = r0 * (1 + 0.15 * np.sin(2 * np.pi * (bpm / 60.0) * i / fps))
        img = np.full((size, size), 120.0)
        img[(xx - cx) ** 2 + (yy - cy) ** 2 <= r ** 2] = 170.0
        img += 5 * rng.standard_normal(img.shape)
        frames[i] = np.clip(img, 0, 255).astype(np.uint8)
    return frames, fps, (cx, cy, r0)


def not_implemented_skip(fn, *args, **kwargs):
    """Fonksiyon henüz yazılmadıysa testi atla (başarısız sayma)."""
    try:
        return fn(*args, **kwargs)
    except NotImplementedError:
        pytest.skip(f"{fn.__module__}.{fn.__name__} henüz yazılmadı")


@pytest.fixture
def heart_signal():
    return make_heart_signal()


@pytest.fixture
def heart_video():
    return make_heart_video()
