import json

#===== Simulated API responses ====

raw_members = [
    {"name": "Tony Njenga", "steps": 9500, "protocol": "OMAD", "sleep": 7.0, "cold shower": True},
    {"name": "Mike Dawa", "steps": 11000, "protocol": "2MAD", "sleep": 6.5, "cold shower": False},
    {"name": "Joseph Sitati", "steps": 8500, "protocol": "OMAD", "sleep": 8.0, "cold shower": True},
    {"name": "Sheila Wafula", "steps": 7000, "protocol": "2MAD", "sleep": 5.5, "cold shower": False},
    {"name": "David Mwangi", "steps": 12000, "protocol": "OMAD", "sleep": 8.5, "cold shower": True},
    {"name": "Grace Wanjiku", "steps": 9000, "protocol": "2MAD", "sleep": 6.0, "cold shower": True},
]
daily_steps = [53000, 63000, 48000, 55000, 60500, 70000, 65300]
day_list  = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
skills_list = [
            {"name": "carpentry", "instructor": "John Mwaniki", "enrolled": 12},
            {"name": "baking", "instructor": "Jane Wanjiru", "enrolled": 10},
            {"name": "gardening", "instructor": "Peter Otieno", "enrolled": 7},
            {"name": "sewing", "instructor": "Lucy Njeri", "enrolled": 13},
            {"name": "plumbing", "instructor": "David Kimani", "enrolled": 9},
        ]

#===== Processing the data ======
STEP_GOAL = 10000
goal_achieved = [m for m in raw_members if m["steps"] >= STEP_GOAL]
average_steps = round(sum(m["steps"] for m in raw_members) / len(raw_members))
showers = sum(1 for m in raw_members if m["cold shower"] is True)
best_day = day_list[daily_steps.index(max(daily_steps))]
top_skill = max(skills_list, key=lambda s: s["enrolled"])

#===== Output the results ======
W = 52
print('=' * W)
print(f"  DASHBOARD  |  Week 2025-W45")
print('=' * W)

print(f"\n SECTION 1: MEMBERS METRICS")
print(f"  {'Total Members:':<25} {len(raw_members)}")
print(f"  Hit {STEP_GOAL:,} step goal:")
print(f"  Hit {STEP_GOAL:,} step goal:     {len(goal_achieved)}/{len(raw_members)}")
print(f"  {'Average steps:':<25} {average_steps:,}")
print(f"  {'Cold showers today:':<25} {showers}/{len(raw_members)}")
print(f"  Goal hitters: {', '.join(m['name'] for m in goal_achieved)}")

print(f"\n  SECTION 2: WEEKLY STEPS")
for day, total in zip(day_list, daily_steps):
    bar = "#" * (total // 5000)
    print(f"  {day:4} {total:>7,}  {bar}")
print(f"  Best day: {best_day} ({max(daily_steps):,} total steps)")
print(f"  Week avg: {round(sum(daily_steps) / len(daily_steps)):,} steps/day")

print(f"\n  SECTION 3: ACTIVE SKILLS")
for s in sorted(skills_list, key=lambda x: x["enrolled"], reverse=True):
    print(f"  {s['name']:15} {s['enrolled']} enrolled")
print(f"  Most popular: {top_skill['name']} ({top_skill['enrolled']} enrolled)")

print(f"\n{'=' * W}")

# JSON export
export = {
    "week": "2025-W45",
    "members": {"total": len(raw_members), "goal_met": len(goal_achieved), "avg_steps": average_steps},
    "weekly": {"best_day": best_day, "total_steps": sum(daily_steps)},
    "skills": {"active": len(skills_list), "most_popular": top_skill["name"]}
}
print("\nJSON export:")
print(json.dumps(export, indent=2))