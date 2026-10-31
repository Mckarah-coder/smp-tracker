steps = 7500
sleep_hours = 6
water_glasses = 5
cold_shower = False
pages_read = 15

if steps >= 10000:
    print("Excellent. 10000 steps exceeded.")
elif steps >= 7500:
    print(f"Good. You need {10000 - steps} more steps to reach 10000.")
else:
    print(f"Needs work. You need {7500 - steps} more steps to reach 7500.") 

if sleep_hours >= 7 and water_glasses >= 8:     
    print("Good. 7 hours of sleep and 8 glasses of water achieved.")
else:
    print("Low. 7 hours of sleep or 8 glasses of water not reached.")

if pages_read >= 10 and cold_shower:
    print("Good. 10 pages read and cold shower completed.")
else:
    print("Low. 10 pages read or cold shower skipped.")

verdict = steps >= 7500 and sleep_hours >= 7 and water_glasses >= 8 and pages_read >= 10 and cold_shower
print(f"Summary verdict: {'Pass' if verdict else 'Needs Improvement'}.")