def predict_delivery_risk(crew_size, days_remaining, tasks_left):
    # efficiency: tasks per worker per day needed
    efficiency = tasks_left / (crew_size * days_remaining)
    if efficiency > 1.5:
        return "High risk: not enough time or crew"
    elif efficiency > 0.8:
        return "Medium risk: tight but possible"
    else:
        return "Low risk: on track"

projects = [
    ("Westlands Office Fit-out", 3, 5, 25),
    ("Karen Tiling Contract", 4, 10, 18),
    ("Industrial Steel Doors", 2, 3, 12),
]

print("Project Risk Assessment:")
print("-" * 45)
for name, crew, days, tasks in projects:
    risk = predict_delivery_risk(crew, days, tasks)
    print(f"{name}")
    print(f"  Crew: {crew} | Days left: {days} | Tasks: {tasks}")
    print(f"  Result: {risk}")
    print()