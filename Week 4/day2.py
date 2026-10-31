def safe_log_entry(data):
    try:
        steps = int(data["steps"])
    except (ValueError, KeyError):
        ("invalid steps data. skipping entry.")
        return None

    water = data.get("water", 0)
    protocol = data.get("protocol", "unknown")

    print(f"steps: {steps} | water: {water} | protocol: {protocol}")
    return steps

entries = [
    {"steps": "10000", "water": "8", "protocol": "OMAD"},
    {"steps": "8000", "protocol": "2MAD"},
    {"steps": "nine thousand", "water": "9", "protocol": "Autophagy Marathon"},
    {"steps": "11000", "water": "7"}
]

results = [safe_log_entry(entry) for entry in entries]
valid = [result for result in results if result is not None]
print(f"\nTotal valid entries: {len(valid)}")
