# Safe Key Access with .get()
records = [
    {"name": "Patrick Njiru", "steps": 9100, "water_glasses": 7},
    {"name": "Grace Achieng", "steps": 8400},           # no water logged
    {"name": "Brian Kamau",   "steps": 10200, "water_glasses": 9},
]

for r in records:
    water = r.get("water_glasses", "not logged")
    print(f"{r['name']}: steps={r['steps']}, water={water}")
print()

# Filtering API Results
logs = [
    {"name": "James Omondi",  "steps": 9200,  "protocol": "OMAD"},
    {"name": "Sandra Weru",   "steps": 10500, "protocol": "2MAD"},
    {"name": "Patrick Njiru", "steps": 8100,  "protocol": "OMAD"},
    {"name": "Grace Achieng", "steps": 11000, "protocol": "OMAD"},
    {"name": "Brian Kamau",   "steps": 7400,  "protocol": "2MAD"},
    {"name": "Kevin Mwangi",  "steps": 10800, "protocol": "OMAD"},
]

# 2MAD users who hit 8,000 steps
goal_hitters = [
    r for r in logs
    if r["protocol"] == "2MAD" and r["steps"] >= 8000
]

print("2MAD users who hit 8k steps:")
for r in goal_hitters:
    print(f"  {r['name']}: {r['steps']} steps")