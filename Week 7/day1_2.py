import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Weekly data: [feed_kg, deaths]
# Label: 1 = hit 300 eggs that week, 0 = did not
X = np.array([
    [18.5, 0], [18.0, 1], [19.2, 0], [18.8, 0], [17.5, 2],
    [18.6, 0], [19.0, 0], [20.1, 0], [17.2, 3], [19.5, 0],
    [18.3, 1], [19.8, 0], [17.0, 2], [18.7, 0], [20.0, 0],
    [16.8, 4], [19.1, 0], [18.4, 0], [17.9, 1], [19.6, 0],
])
y = np.array([1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1])

print(f"Features shape: {X.shape}")
print(f"Labels shape:   {y.shape}")

# Step 2: Split into train/test sets and train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(X_train, y_train)

# Step 3: Evaluate the model on the test set
accuracy = clf.score(X_test, y_test)
print(f"\nModel accuracy: {accuracy:.0%}")

# Predict for new weeks
new_weeks = np.array([
    [19.0, 0],  # good feed, no deaths
    [17.0, 3],  # low feed, 3 deaths
    [18.5, 1],  # normal feed, 1 death
])
preds = clf.predict(new_weeks)
labels = {1: "Hit 300 eggs", 0: "Below target"}
print("\nPredictions:")
for inputs, pred in zip(new_weeks, preds):
    print(f"  Feed={inputs[0]}kg  Deaths={int(inputs[1])} => {labels[pred]}")