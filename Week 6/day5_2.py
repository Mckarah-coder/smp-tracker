import pandas as pd
import numpy as np

steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200, 8900, 10800, 9100, 11200, 7900, 10000, 9700, 9500, 10300, 8600, 11500, 8200, 9800, 10600, 9000, 10100, 8400, 10900, 7500, 9600, 10400])
bench = np.array([80, 82, 78, 85, 80, 83, 84, 81, 85, 80, 86, 79, 84, 83, 82, 86, 79, 88, 81, 85, 87, 82, 86, 80, 87, 79, 84, 86])
sleep = np.array([7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0, 6.0, 8.5, 7.0, 7.5, 9.0, 7.0, 7.5, 7.0, 8.0, 6.5, 7.5, 8.0, 7.0, 8.5, 7.0, 7.5, 6.5, 8.0, 9.5, 7.0, 8.0])

print("=== 28-Day NumPy Analysis ===")
print(f"\nsteps:")
print(f"  Mean:       {np.mean(steps):,.0f}")
print(f"  std dev     {np.std(steps):,.0f}")
print(f"  25th pctile {np.percentile(steps, 25):,.0f}")
print(f"  75th pctile {np.percentile(steps, 75):,.0f}")
print(f"  Days 10k+   {np.sum(steps >= 10000)}/28")

print(f"\nBench press:")
print(f"  Mean:       {np.mean(bench):.1f} kg")
print(f"  Max:        {np.max(bench)} kg  (Day {np.argmax(bench)+1})")
print(f"  Trend:      {'increasing' if bench[-7:].mean() > bench[:7].mean() else 'flat/decreasing'}")

# Correlation
corr = np.corrcoef(steps, bench)[0, 1]
print(f"\ncorrelation steps vs bench: {corr:.3f}")
print(f"interpretation: {'positive relationship' if corr > 0.3 else 'weak/no relationship'}")
