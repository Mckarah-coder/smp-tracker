import csv
import io 

csv_data = """day,steps,protocol
Monday,8500,OMAD
Tuesday,7000,2MAD
Wednesday,9500,OMAD
Thursday,6000,AUTOHAGY MARATHON
Friday,8300,2MAD
Saturday,10000,OMAD
Sunday,9000,2MAD"""

file = io.StringIO(csv_data)
reader = csv.DictReader(file)

valid_steps = []
for row in reader:
    steps = int(row["steps"])
    if steps >= 7000:
        valid_steps.append(steps)
        print(f"{row['day']} : {steps} steps ({row['protocol']})")
    else:   
        print(f"{row['day']} : {steps} steps - invalid")

avg_steps = sum(valid_steps) / len(valid_steps)
print(f"\nAverage steps (valid days) for the week is {round(avg_steps)}")
