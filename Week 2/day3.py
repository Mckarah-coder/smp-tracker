my_log = {"steps": 9000, "water_glasses": 8, "fasting_protocol": "OMAD", "cold_shower": True, "sleep_hours": 7.0}

for key, value in my_log.items():
    print(f"{key}: {value}")

print()

if int(str(my_log["steps"])) >= 8000:
    print("steps goal met!")
else:
    print("steps goal not met!")

