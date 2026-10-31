# 1. Functions
def greet(name):
    return f"Hello, {name}. Welcome to the program."

print(greet("Mark"))
print(greet("Moses")) 
print()

# 2. Default Parameters
def power(base, exp=2):
    return base ** exp

print(power(3))
print(power(4, 3))
print()

# 3. List Comprehensions
evens = [n for n in range (1, 31) if n % 2 == 0]
print(evens)
print()

squares = [n**2 for n in evens]
print(squares)
print()

# 4. Challenge
def analyse(scores):
    return {
        "average": sum(scores) / len(scores),
        "highest": max(scores),
        "lowest" : min(scores)
    }

results = analyse([82, 72,95,65,85])
for k, v in results.items():
    print(f"{k} : {v}")
print()

# Code Challenge
def greet (name):
    return (f"Hello, {name}!")

print(greet("Amerix"))
print(greet("SMP Member"))
print(greet("Guest"))