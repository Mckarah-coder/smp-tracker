import pandas as pd

data = {
    "day":          ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "cows":         [12, 12, 11, 12, 11, 12, 12],
    "milk_litres":  [248, 252, 239, 255, 241, 260, 257],
    "feed_kg":      [185, 188, 176, 190, 180, 195, 192],
    "shed":         ["A", "A", "A", "B", "B", "B", "A"],
}

df = pd.DataFrame(data)
df["revenue_kes"] = df["milk_litres"] * 80

print("Weekly cow and milk production log:")
print(df.to_string())

print("\nShape(rows,cols):", df.shape)
print("\nColumns:", list(df.columns))
print("\nData types:")
print(df.dtypes)
print("\nFirst 4 rows:")
print(df.head(4).to_string())

print("\nMilk and feed columns:\n")
print(df[["milk_litres", "feed_kg"]].to_string())
print("\nFirst row (iloc):")
print(df.iloc[0].to_string())
print("\nFirst three rows (iloc):")
print(df.iloc[:3].to_string())

print("\nSummary statistics:")
print(df[["cows", "milk_litres", "feed_kg"]].describe().round(1).to_string())

print(f"\nAverage daily milk (liters): {df['milk_litres'].mean():.1f}")
print(f"Total milk this week (liters): {df['milk_litres'].sum()}")
print(f"Weekly revenue: KES {df['revenue_kes'].sum()}")
print(f"Maximum daily milk (liters): {df['milk_litres'].max()}")
print(f"Minimum daily milk (liters): {df['milk_litres'].min()}")