"""Yazılım sonuçlarını MBG'nin elle saydığı atımlarla karşılaştırır (başarı kriteri 3).

Kullanım:
    python scripts/validate.py data/processed/sonuclar.csv data/ground_truth/elle_sayim.csv

elle_sayim.csv sütunları: file,manual_bpm
Çıktı: Pearson r, ortalama mutlak hata, Bland-Altman sınırları. Hedef: r >= 0.90
"""

import argparse

import numpy as np
import pandas as pd
from scipy import stats


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("results_csv")
    ap.add_argument("manual_csv")
    args = ap.parse_args()

    df = pd.read_csv(args.results_csv).merge(pd.read_csv(args.manual_csv), on="file")
    if len(df) < 3:
        raise SystemExit("Karşılaştırma için en az 3 eşleşen video gerekli.")

    r, p = stats.pearsonr(df["bpm"], df["manual_bpm"])
    diff = df["bpm"] - df["manual_bpm"]
    mae = diff.abs().mean()
    bias, sd = diff.mean(), diff.std(ddof=1)

    print(f"Video sayısı       : {len(df)}")
    print(f"Pearson r          : {r:.3f} (p={p:.4f})  {'BAŞARILI' if r >= 0.90 else 'HEDEFİN ALTINDA'}")
    print(f"Ortalama mutlak hata: {mae:.2f} BPM")
    print(f"Bland-Altman       : sapma {bias:.2f}, uyum sınırları [{bias - 1.96 * sd:.2f}, {bias + 1.96 * sd:.2f}]")
    print("\nEn büyük farklar:")
    print(df.assign(fark=diff).reindex(diff.abs().sort_values(ascending=False).index).head(5)
            [["file", "bpm", "manual_bpm", "fark"]].to_string(index=False))


if __name__ == "__main__":
    main()
