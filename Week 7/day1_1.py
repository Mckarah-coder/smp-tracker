import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


X = np.array([
    [7.5, 7, 80], [8.0, 8, 82], [6.5, 6, 78], [7.0, 9, 85],
    [9.0, 8, 80], [7.5, 7, 83], [8.0, 8, 84], [6.0, 6, 81],
    [8.5, 9, 85], [7.0, 8, 80], [7.5, 8, 86], [9.0, 7, 79],
    [7.0, 9, 84], [7.5, 8, 83], [7.0, 7, 82], [8.0, 8, 86],
    [6.5, 6, 79], [7.5, 9, 88], [8.0, 8, 81], [7.0, 7, 85],
    [8.5, 9, 87], [7.0, 8, 82], [7.5, 8, 86], [6.5, 6, 80],
    [8.0, 9, 87], [9.5, 7, 79], [7.0, 8, 84], [8.0, 9, 86],
])
steps = np.array([
    9200, 10500, 8800, 11000, 7600, 9400, 10200, 8900, 10800, 9100,
    11200, 7900, 10000, 9700, 9500, 10300, 8600, 11500, 8200, 9800,
    10600, 9000, 10100, 8400, 10900, 7500, 9600, 10400,
])

# Convert step counts to binary labels: 1 = hit goal, 0 = missed
y = (steps >= 10000).astype(int)
print("Label distribution (1=hit goal, 0=missed):")
print(f"  Hit goal:  {y.sum()}/28 days")
print(f"  Missed:    {(y == 0).sum()}/28 days")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

two_feature_model = RandomForestClassifier(n_estimators=10, random_state=42)
two_feature_model.fit(X_train[:, :2], y_train)
two_feature_accuracy = two_feature_model.score(X_test[:, :2], y_test)

three_feature_model = RandomForestClassifier(n_estimators=10, random_state=42)
three_feature_model.fit(X_train, y_train)
three_feature_accuracy = three_feature_model.score(X_test, y_test)

print(f"\nAccuracy with sleep and water: {two_feature_accuracy:.0%}")
print(f"Accuracy with sleep, water, and bench: {three_feature_accuracy:.0%}")
print(f"Accuracy improved: {'Yes' if three_feature_accuracy > two_feature_accuracy else 'No'}")

new_days = np.array([[8.0, 8, 85], [6.0, 5, 78], [9.0, 9, 88]])
preds = three_feature_model.predict(new_days)
labels = {1: "Goal hit", 0: "Below goal"}
print("\nPredictions for new days:")
for inputs, pred in zip(new_days, preds):
    print(f"  Sleep={inputs[0]}h, Water={int(inputs[1])}, Bench={inputs[2]}kg => {labels[pred]}")

feature_names = ["sleep_hours", "water_glasses", "bench_press_kg"]
importances = three_feature_model.feature_importances_

print("\nFeature importances (how much each feature contributes):")
for name, imp in sorted(zip(feature_names, importances), key=lambda x: -x[1]):
    bar = "#" * int(imp * 40)
    print(f"  {name:<18} {imp:.3f}  {bar}")