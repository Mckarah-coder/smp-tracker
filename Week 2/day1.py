week_steps = [9400, 7200, 10300, 6500, 8900, 9800, 11100]

for steps in week_steps:
    if steps >= 8000:
        print(steps, "steps - Goal achieved")
    else:
        print(steps, "steps - Goal not achieved")

print("Days tracked:", len(week_steps))   