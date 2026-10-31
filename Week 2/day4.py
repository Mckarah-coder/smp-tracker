week_log = [
    {"day": "Monday",    "steps": 10000,  "protocol": "OMAD"},
    {"day": "Tuesday",   "steps": 9500, "protocol": "2MAD"},
    {"day": "Wednesday", "steps": 8500,  "protocol": "OMAD"},
    {"day": "Thursday",  "steps": 7400, "protocol": "Autophagy Marathon"},
    {"day": "Friday",    "steps": 11500,  "protocol": "OMAD"},
]

total_steps = 0
for log in week_log:
    total_steps += log["steps"]
    print(log["day"], "|", log["steps"]), "steps", "|", log["protocol"] # type: ignore

average_steps = total_steps / len(week_log)
print("\nAverage steps for the week:", average_steps)