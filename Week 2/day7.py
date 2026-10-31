# Habit Tracker

#Habit log list storing daily habits and their completion status
habit_logs = [
    {"date": "2026-09-01", "steps": 10000, "fasting_protocol": "OMAD", "water_glasses": 8, "habit_completed": True},
    {"date": "2026-09-02", "steps": 8000, "fasting_protocol": "OMAD", "water_glasses": 6, "habit_completed": False},
    {"date": "2026-09-03", "steps": 12000, "fasting_protocol": "2MAD", "water_glasses": 9, "habit_completed": True},
    {"date": "2026-09-04", "steps": 11000, "fasting_protocol": "Autophagy Marathon", "water_glasses": 7, "habit_completed": True}
]

# Log a New Day
new_habit_entry = {
    "date": "2026-09-05",
    "steps": 7000,
    "fasting_protocol": "OMAD",
    "water_glasses": 8,
    "habit_completed": False
}
habit_logs.append(new_habit_entry)

# View All Entries
print("=== Habit Tracker Logs ===")
for i, log in enumerate(habit_logs):
    print(f"\nEntry {i + 1};")
    print(f"Date: {log['date']}")
    print(f"Steps: {log['steps']}")
    print(f"Fasting Protocol: {log['fasting_protocol']}")
    print(f"Water Glasses: {log['water_glasses']}")
    print(f"Habit Completed: {log['habit_completed']}")

# Search by Fasting Protocol
search_protocol = "OMAD"
print(f"\n=== Entries with Fasting Protocol: {search_protocol} ===")
found_protocol = False

for log in habit_logs:
    if log["fasting_protocol"] == search_protocol:
        found_protol = True
        print(f"\nDate: {log['date']}")
        print(f"Steps: {log['steps']}")
        print(f"Water Glasses: {log['water_glasses']}")
        print(f"Habit Completed: {log['habit_completed']}")
        
if not found_protocol:
    print(f"No entries found with Fasting Protocol: {search_protocol}")

# Search by Date
search_date = "2026-09-02"
print(f"\n=== Entries for Date: {search_date} ===")
found_date = False

for log in habit_logs:
    if log["date"] == search_date:
        found_date = True
        print(f"\nFasting Protocol: {log['fasting_protocol']}")
        print(f"Steps: {log['steps']}")
        print(f"Water Glasses: {log['water_glasses']}")
        print(f"Habit Completed: {log['habit_completed']}")

if not found_date:
    print(f"No entries found for Date: {search_date}")

# Summary
print(f"\nTotal Days Tracked: {len(habit_logs)}")