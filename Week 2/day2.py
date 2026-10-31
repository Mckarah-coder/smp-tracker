steps = [8800, 6500, 11000, 9200, 7300]
steps.append(10500)
steps.remove(6500)
steps.sort(reverse=True)

print("Final list:", steps)

#count days with more than 9000 steps
count = 0
for step in steps:
    if step > 9000:
          count += 1  
        
print("Days with more than 9000 steps:", count)