# Store your values
exercises = 6
sets_per_exercise = 4
reps_per_set = 10
average_weight_per_rep_kg = 60
session_duration_in_minutes = 45

# Add the rest below
total_sets = exercises * sets_per_exercise
total_reps = total_sets * reps_per_set
total_volume_lifted_kg = total_reps * average_weight_per_rep_kg
reps_per_minute = total_reps // session_duration_in_minutes 

# Calculate and print your report
print("===FULL SESSION REPORT===")
print(f"Total Sets : {total_sets}")
print(f"Total reps : {total_reps}")
print(f"Total Volume : {total_volume_lifted_kg} kg")
print(f"Reps per minute : {reps_per_minute}")
print(f"Exceeded 10,000 kg target : {total_volume_lifted_kg > 10000}")