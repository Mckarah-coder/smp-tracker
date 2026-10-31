def weekly_report(name, step_list, goal=8000):
    day_on_target = 0
    for s in step_list:
        if s >= goal:
            day_on_target += 1
    avg = sum(step_list) / len(step_list)
    print(f"=== Weekly Report for {name} ===")
    print (f"Days Tracked : {len(step_list)}")
    print (f"Days on Target : {day_on_target}")
    print (f"Average Steps : {round(avg, 0)}")
    print()

weekly_report("Alice", [7500, 8500, 9000, 8000, 9500, 7000, 10000])
weekly_report("Bob", [6000, 7000, 8000, 9000, 10000, 11000, 12000])