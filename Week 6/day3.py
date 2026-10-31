import pandas as pd

df = pd.DataFrame({
    "client":   ["Wanjiru", "Otieno", "Kamau", "Mwangi", "Njeri",  "Odhiambo", "Achieng", "Bett"],
    "item":     ["gate",    "grills", "frame", "gate",   "grills", "tank stand","frame",   "gate"],
    "material": ["mild steel","angle iron","hollow tube","mild steel","angle iron","mild steel","hollow tube","mild steel"],
    "price_kes":[28000, 14500, 9800, 32000, 12000, 18500, 11000, 29500],
    "status":   ["paid","paid","pending","paid","paid","pending","paid","paid"],
    "region":   ["Nairobi","Kiambu","Machakos","Kiambu","Nairobi","Nairobi","Machakos","Kiambu"]
})

# Revenue by region and material
print("\nRevenue by region and material:")
region_material_revenue = df.groupby(["region", "material"])["price_kes"].sum()
by_region_material = region_material_revenue.unstack(fill_value=0)
print(by_region_material)

print("\nTop-earning region for each material:")
max_revenue_by_material = region_material_revenue.groupby("material").transform("max")
top_regions = region_material_revenue[region_material_revenue.eq(max_revenue_by_material)]
top_regions = top_regions.rename("total_kes").reset_index()
print(top_regions.to_string(index=False))