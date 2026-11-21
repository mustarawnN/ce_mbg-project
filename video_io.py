"""Video okuma ve standartlaştırma.

Sorumlu: Ali
"""

from __future__ import annotations

import numpy as np


def get_video_info(path: str) -> dict:
    """Videonun FPS, süre, çözünürlük, codec ve sabit/değişken FPS bilgisini döndürür.

    İpucu: `ffprobe -v error -show_streams -of json <path>` çıktısını okuyun.
    Dönüş örneği: {"fps": 30.0, "duration_s": 20.1, "width": 1280, "height": 720,
                   "codec": "h264", "variable_fps": False}
    """
    raise NotImplementedError


def normalize_video(path: str, target_fps: float | None = None) -> str:
    """Videoyu FFmpeg ile sabit FPS'li, tek formatlı (H.264 .mp4) hale getirir.

    Dönüştürülen dosya config.PROCESSED_DIR altına yazılır ve yolu döndürülür.
    İpucu: ffmpeg -i in.mov -vf fps=<fps> -c:v libx264 -preset veryfast -an out.mp4
    """
    raise NotImplementedError


def read_frames(path: str, max_frames: int | None = None) -> tuple[np.ndarray, float]:
    """Videoyu gri tonlu kareler olarak okur.

    Dönüş: (frames (T, H, W) uint8, fps)
    """
    raise NotImplementedError
