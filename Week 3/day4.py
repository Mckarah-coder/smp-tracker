people = [
    {"name": "John", "steps": [8000, 9500, 9800, 8000, 7200, 8500, 7800]},
    {"name": "Mary", "steps": [8500, 9000, 8800, 9200, 8600, 9400, 9100]},
    {"name": "James", "steps": [9000, 11500, 9800, 11000, 10300, 11000, 10800]},
    {"name": "Mark", "steps": [8900, 9800, 10500, 9500, 8800, 9000, 10700]},
]

# Find all step counts above 10,000.
all_steps = [step for person in people for step in person["steps"]]
high_steps = [step for step in all_steps if step > 10000] 
print("Steps above 10,000:", high_steps)

# Find people whose average steps are above 9,000.
high_average_names = [person["name"] for person in people if sum(person["steps"]) / len(person["steps"]) > 9000]
print("High average performers:", high_average_names)