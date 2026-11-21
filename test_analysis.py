"""Sinyal analizi testleri. Sorumlu: Mustafa"""

import numpy as np
import pytest

from conftest import make_heart_signal, not_implemented_skip
from daphniavision.analysis import bpm, dose_response, filtering, rhythm


@pytest.mark.parametrize("true_bpm", [150, 240, 330])
def test_bpm_within_3(true_bpm):
    sig, fps = make_heart_signal(bpm=true_bpm)
    filtered = not_implemented_skip(filtering.bandpass, not_implemented_skip(filtering.detrend, sig), fps)
    freqs, power = not_implemented_skip(bpm.spectrum, filtered, fps)
    est = not_implemented_skip(bpm.bpm_from_spectrum, freqs, power)
    assert abs(est - true_bpm) <= 3


def test_beat_count(heart_signal):
    sig, fps = heart_signal  # 240 BPM, 20 s -> 80 atım
    filtered = not_implemented_skip(filtering.bandpass, not_implemented_skip(filtering.detrend, sig), fps)
    beats = not_implemented_skip(bpm.detect_beats, filtered, fps, 240.0)
    assert abs(len(beats) - 80) <= 2


def test_regular_rhythm_low_cv():
    beats = np.arange(0, 20, 0.25)  # tam düzenli 240 BPM
    m = not_implemented_skip(rhythm.rhythm_metrics, beats)
    assert m["ibi_cv"] < 0.01
    assert m["pauses"] == 0


def test_pause_detected():
    beats = np.concatenate([np.arange(0, 5, 0.25), np.arange(5.75, 10, 0.25)])  # 0.75 s duraksama
    m = not_implemented_skip(rhythm.rhythm_metrics, beats)
    assert m["pauses"] >= 1


def test_ec50_recovers_true_value():
    doses = np.array([0.1, 0.3, 1, 3, 10, 30, 100])
    true = 100 / (1 + (doses / 5.0) ** 1.2)
    fit = not_implemented_skip(dose_response.fit_ec50, doses, true)
    assert abs(fit["ec50"] - 5.0) / 5.0 < 0.1
