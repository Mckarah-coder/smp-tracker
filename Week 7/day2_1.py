import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Features: [quote_kes, job_type_encoded, estimated_job_duration_days]
# Job types: gate=0, window grills=1, door frame=2, roof sheet=3
# Label: 1 = paid, 0 = pending/unpaid
X = np.array([
    [28000, 0, 5], [14500, 1, 3], [9800, 2, 2], [32000, 0, 5],
    [12000, 1, 3], [18500, 0, 5], [11000, 2, 2], [29500, 0, 5],
    [8500, 3, 1], [22000, 1, 3], [35000, 0, 5], [7200, 2, 2],
    [16000, 3, 1], [31000, 0, 5], [13500, 1, 3], [10500, 2, 2],
    [24000, 0, 5], [9000, 3, 1], [27000, 1, 3], [15000, 2, 2],
])
y = np.array([1,1,0,1,1,0,1,1,1,0,1,0,1,1,0,1,1,0,1,0])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("Job payment prediction report:")
print(classification_report(y_test, y_pred, target_names=["Unpaid", "Paid"]))

cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
print("Confusion matrix:")
print("                   Predicted Unpaid  Predicted Paid")
print(f"  Actual Unpaid     {cm[0, 0]:>14}  {cm[0, 1]:>14}")
print(f"  Actual Paid       {cm[1, 0]:>14}  {cm[1, 1]:>14}")

feature_names = ["quote_kes", "job_type_encoded", "estimated_job_duration_days"]
importances = clf.feature_importances_

print("\nFeature importances (how much each feature contributes):")
for name, imp in sorted(zip(feature_names, importances), key=lambda x: -x[1]):
    print(f"  {name:<18} {imp:.3f}")