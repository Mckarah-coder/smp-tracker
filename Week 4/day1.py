import io

# Simulate file: individual line with step count
weekly_steps = """Monday : 8800
Tuesday : 10000
Wednesday : 8500
Thursday : 9000
Friday : 6700
Saturday : 11000
Sunday : 7800
"""
goal = 8000
days_on_goal = 0


f = io.StringIO(weekly_steps)
for line in f:
    line = line.strip()
    if ":" in line:
        day, steps_str = line.split(":", 1)
        steps = int(steps_str.strip())
        status = "Goal hit" if steps >= goal else "Goal not hit"
        print(f"{day}: {steps} - {status}")
        if steps >= goal:
            days_on_goal += 1

print(f"\nDays on goal: {days_on_goal} / 7")
