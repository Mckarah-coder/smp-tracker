import json
from typing import cast

week_report = {
    "name": "Moses",
    "steps": [8500, 7000, 9500, 6000, 8300, 10000],
    "protocols": ["OMAD","2MAD","OMAD","AUTOHAGY MARATHON","2MAD"]
}

# Convert to JSON
json_str = json.dumps(week_report, indent=2)
print("Week report:")
print(json_str)

# Load back and calculate average steps
week_report = json.loads(json_str)
steps = cast(list[int], week_report["steps"])
avg_steps = sum(steps) / len(steps)
print(f"\nAverage steps for {week_report['name']} is {round(avg_steps)}")
