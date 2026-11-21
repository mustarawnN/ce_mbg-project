"""Kalp bölgesinden 1 boyutlu zaman sinyalinin çıkarılması.

Sorumlu: Vahit
"""

from __future__ import annotations

import numpy as np

from daphniavision.schemas import HeartSignal

METHODS = ("mean_intensity", "frame_diff", "optical_flow")


def mean_intensity(frames: np.ndarray, roi_mask: np.ndarray) -> np.ndarray:
    """ROI içindeki ortalama parlaklık. En basit ve en hızlı yöntem. Dönüş: (T,)"""
    raise NotImplementedError


def frame_diff(frames: np.ndarray, roi_mask: np.ndarray) -> np.ndarray:
    """ROI içinde ardışık kareler arasındaki mutlak fark ortalaması. Dönüş: (T,)"""
    raise NotImplementedError


def optical_flow(frames: np.ndarray, roi_mask: np.ndarray) -> np.ndarray:
    """ROI içindeki hareket büyüklüğü (cv2.calcOpticalFlowFarneback). En yavaş yöntem. Dönüş: (T,)"""
    raise NotImplementedError


def signal_snr(signal: np.ndarray, fps: float) -> float:
    """Kalp bandındaki tepe gücünün bant dışı güce oranı. Yöntem seçiminde kullanılır."""
    raise NotImplementedError


def extract_best_signal(
    frames: np.ndarray,
    fps: float,
    roi_mask: np.ndarray,
    heatmap: np.ndarray,
    method: str | None = None,
    roi_auto: bool = True,
) -> HeartSignal:
    """method verilmişse onu kullanır; None ise tüm yöntemleri dener, en yüksek SNR'liyi seçer."""
    raise NotImplementedError
