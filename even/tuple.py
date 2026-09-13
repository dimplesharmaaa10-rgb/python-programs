employees = (
    "Amit", "Rahul", "Priya", "Neha", "Amit",
    "Rohan", "Priya", "Karan", "Sneha", "Rahul",
    "Amit", "Vikas", "Neha", "Riya", "Karan",
    "Arjun", "Sneha", "Priya", "Rohan", "Amit"
)
print("Name and Frequency:")
for name in employees:
    if name not in employees[:employees.index(name)]:
        print(name, ":", employees.count(name))
distinct_names = ()
for name in employees:
    if name not in distinct_names:
        distinct_names = distinct_names + (name,)
print("\nDistinct Names:")
print(distinct_names)
max_frequency = 0
max_name = ""
for name in distinct_names:
    if employees.count(name) > max_frequency:
        max_frequency = employees.count(name)
        max_name = name
print("\nEmployee having maximum frequency:")
print(max_name, "with frequency", max_frequency)
sorted_tuple = tuple(sorted(employees))
print("\nTuple in alphabetical order:")
print(sorted_tuple)
search_name = input("\nEnter employee name to search: ")
if search_name in employees:
    print(search_name, "exists in the tuple")
else:
    print(search_name, "does not exist in the tuple")