import pandas as pd

jobs = [
    {"client": "Kamau", "boxes_used": 30, "price_per_box": 1800},
    {"client": "Mutua", "boxes_used": 48, "price_per_box": 2100},
    {"client": "Odhiambo", "boxes_used": 20, "price_per_box": 1600},
    {"client": "Wanjiru", "boxes_used": 60, "price_per_box": 2200},
]

df = pd.DataFrame(jobs)

print(f"\nTotal: {df['boxes_used'].sum()}")
print(f"Revenue: KES {sum(df['boxes_used'] * df['price_per_box'])}")