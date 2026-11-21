"""Bir klasördeki tüm videoları toplu analiz eder ve sonuçları CSV'ye yazar.

Kullanım:
    python scripts/batch_analyze.py data/raw --out data/processed/sonuclar.csv

Deney bilgileri için klasörde videolarla aynı adlı bir metadata.csv beklenir:
    file,substance,dose,is_control,temperature_c,age_hours,acclimation_min
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd

from daphniavision import pipeline
from daphniavision.schemas import ExperimentMeta

VIDEO_EXT = {".mp4", ".mov", ".avi", ".mkv"}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--out", default="data/processed/sonuclar.csv")
    args = ap.parse_args()

    folder = Path(args.folder)
    meta_csv = folder / "metadata.csv"
    meta_df = pd.read_csv(meta_csv).set_index("file") if meta_csv.exists() else None

    rows = []
    for video in sorted(p for p in folder.iterdir() if p.suffix.lower() in VIDEO_EXT):
        info = meta_df.loc[video.name].to_dict() if meta_df is not None and video.name in meta_df.index else {}
        meta = ExperimentMeta(substance=info.pop("substance", "bilinmiyor"), dose=info.pop("dose", 0.0), **info)
        print(f"Analiz: {video.name}")
        try:
            r = pipeline.run(str(video), meta)
        except Exception as e:  # tek video hatası tüm işi durdurmasın
            print(f"  HATA: {e}")
            continue
        m = r.metrics
        rows.append({"file": video.name, "substance": meta.substance, "dose": meta.dose,
                     "bpm": m.bpm, "beat_count": m.beat_count, "ibi_cv": m.ibi_cv,
                     "pauses": m.pauses, "reliability": m.reliability})

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(args.out, index=False)
    print(f"{len(rows)} video -> {args.out}")


if __name__ == "__main__":
    main()
