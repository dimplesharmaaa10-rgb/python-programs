fruits = {"apple", "banana", "mango", "orange", "grapes", "watermelon", "guava", "pineapple", "papaya", "pomegranate"}
summer_fruits = {"mango", "watermelon", "guava", "papaya", "litchi"}
winter_fruits = {"orange", "grapes", "apple", "pomegranate", "strawberry"}
print("All fruits:", fruits)
print("Summer fruits:", summer_fruits)
print("Winter fruits:", winter_fruits)
print("Fruits present in both fruits and winter fruits:", fruits.intersection(winter_fruits))
print("Fruits present only in summer fruits:", summer_fruits.difference(fruits))
print("Fruits present in summer and winter fruits but not in fruits:", summer_fruits.intersection(winter_fruits).difference(fruits))
if "orange" in fruits:
    print("Orange is present in fruits.")
else:
    print("Orange is not present in fruits.")
if "pineapple" in fruits:
    print("Pineapple is present in fruits set.")
elif "pineapple" in summer_fruits:
    print("Pineapple is present in summer fruits set.")
elif "pineapple" in winter_fruits:
    print("Pineapple is present in winter fruits set.")
else:
    print("Pineapple is not present in any set.")