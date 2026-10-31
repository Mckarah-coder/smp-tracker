daily_steps = [8200, 5100, 11300, 6800, 9400, 4200, 10100]
target_steps = 8000
minimum_steps = 5000

print("===DAILY STEPS CHECKER===")
for steps in daily_steps:
    print(f"checking: {steps} steps")
    if steps >= target_steps:
        print(f"target hit on this day: {steps} steps")
    else:
        print(f"target not hit on this day: {steps} steps")

print("\n=== WEEKLY STEPS AVERAGE (SKIPPING < 5000) ===")
total = 0
valid_days = 0

for steps in daily_steps:
    if steps < minimum_steps:
        print(f"skipping {steps} (below minimum steps)")
        continue
    total += steps
    valid_days += 1

weekly_average = total // valid_days if valid_days > 0 else 0

print(f"\nValid days: {valid_days}")
print(f"Total steps(valid days): {total}")
print(f"Average steps: {weekly_average:.0f}")

print("\n=== CONSECUTIVE TARGET STREAK ===")
Streak = 0
day = 0

while day < len(daily_steps) and daily_steps[day] >= target_steps:
    Streak += 1
    day += 1    

print(f"Consecutive target streak: {Streak} days")

print("\n===Weekly Summary===")
print(f"Total Valid Days (>= {minimum_steps} steps): {valid_days}")
print(f"Average Steps (Valid Days): {weekly_average}")
print(f"Consecutive Target Streak: {Streak} days")
