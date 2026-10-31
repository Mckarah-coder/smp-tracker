def day_report(steps, water, protocol):
    print("=== DAILY REPORT ===")
    print(f"Steps taken: {steps}")
    print(f"Water consumed: {water} glasses")
    print(f"Protocol followed: {protocol}")
    print()

def hit_goal(steps):
    return steps >= 8000

day_report(7500, 8, "OMAD")
day_report(8500, 10, "2MAD")
day_report(9000, 12, "Autophagy Marathon")

print("Goal hit (7500):", hit_goal(7500))  
print("Goal hit (8500):", hit_goal(8500))  
print("Goal hit (9000):", hit_goal(9000))  