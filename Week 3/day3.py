import math
import random


def generate_week():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    total = 0
    goal_days = 0

    for day in days:
        steps = random.randint(6000, 12000)
        total += steps
        if steps >= 8000:
            goal_days += 1
        print(f" {day}: {steps} steps")

    average_steps = math.floor(total / len(days))
    print(f"\nAverage steps : {average_steps}")
    print(f"Days on goal : {goal_days} / {len(days)}")

generate_week()