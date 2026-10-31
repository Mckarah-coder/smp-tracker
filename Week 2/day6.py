#List Operations
fruits = ["apple", "banana", "orange", "grape", "kiwi"]
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
fruits.append("mango")
print(fruits)
fruits.sort(reverse=True)
print(fruits)

#Dictionary Work
print()
student = {"Name": "John", "Age": 20, "Grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")

#Nested Data
print()
students = [
    {"Name": "John", "Grade": "A"},
    {"Name": "Alice", "Grade": "B"},
    {"Name": "Bob", "Grade": "C"}
]
for s in students:
    print(f"{s['Name']}:{s['Grade']}")

#Challenge- Simple Phonebook
print()
phonebook = {"Mark": "0722332192", "John": "0722332193", "Alice": "0722332194"}
print("===PHONE BOOK===")
for name, number in phonebook.items():
    print(f"{name}: {number}")
