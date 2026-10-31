import math
from datetime import date

#==== DATA ====
client_name = "Mark"
weight_kg = 72
height_m = 1.75
weekly_steps = [10500, 8000, 7500, 9200, 9800, 11500, 12000]
protocols = ["OMAD", "2MAD", "OMAD", "Autophagy Marathon", "OMAD", "2MAD", "OMAD"]
step_goal = 9000

#==== FUNCTIONS ====
def calculate_bmi(weight_kg, height_m):
    return round(weight_kg / (height_m ** 2), 1)

def bmi_category(bmi):
    if bmi < 18.5: return "Underweight"
    elif bmi < 25: return "Normal weight"
    elif bmi < 30:return "Overweight"
    else:return "Obese"

def weekly_step_summary(steps, goal= step_goal):
    return{
        "days_on_goal": len([step for step in steps if step >= goal]),
        "average": round(sum(steps) / len(steps)),
        "best": max(steps),
        "worst": min(steps)
    }

def estimate_calories(steps, rate=0.04):
    return math.floor (steps * rate)

def protocol_summary(protocol_list):
    return{protocol: protocol_list.count(protocol) for protocol in set(protocol_list)}

#==== MAIN REPORT ====
today = date.today().strftime("%B %d, %Y")
bmi = calculate_bmi(weight_kg, height_m)
steps_report = weekly_step_summary(weekly_steps, step_goal)
total_cals = sum(estimate_calories(step) for step in weekly_steps)
protocol_report = protocol_summary(protocols)

print("=" * 50) 
print(f" WEEKLY REPORT: {client_name.upper()}")
print(f" Date: {today}")
print("=" * 50)
print("\nBODY")
print(f"  Weight : {weight_kg} kg")
print(f"  BMI : {bmi} ({bmi_category(bmi)})")
print(f"\nSTEPS (Goal: {step_goal})")
print(f"  Days on goal: {steps_report['days_on_goal']}/{len(weekly_steps)}")
print(f"  Average     : {steps_report['average']} steps/day")
print(f"  Best day    : {steps_report['best']} steps")
print(f"  Worst day   : {steps_report['worst']} steps")
print(f"  Cals burned  : {total_cals} kcal")
print("\nPROTOCOL BREAKDOWN")
for protocol, days in protocol_report.items():
    print(f"  {protocol}: {days} days")
print("\n" + "=" * 50)