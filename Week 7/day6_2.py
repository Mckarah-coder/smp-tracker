def predict_goat_health(name, weight_loss_kg, feed_drop_pct, age_years):
    risk_score = 0
    if weight_loss_kg > 3:
        risk_score += 2
    elif weight_loss_kg > 1.5:
        risk_score += 1
    if feed_drop_pct > 30:
        risk_score += 2
    elif feed_drop_pct > 15:
        risk_score += 1
    if age_years > 8:
        risk_score += 1

    if risk_score >= 4:
        return "High risk: call vet"
    elif risk_score >= 2:
        return "Medium risk: monitor closely"
    else:
        return "Low risk: healthy"

herd = [
    ("Simba",   4.2, 35, 3),
    ("Kijana",  0.5,  8, 2),
    ("Mzee",    2.1, 20, 9),
    ("Damu",    3.8, 40, 5),
    ("Furaha",  0.8, 10, 4),
]

print("Goat Health Assessment:")
print("-" * 45)
for name, wl, fd, age in herd:
    result = predict_goat_health(name, wl, fd, age)
    print(f"{name}: weight loss {wl}kg | feed drop {fd}% | age {age}yrs")
    print(f"  Assessment: {result}\n")