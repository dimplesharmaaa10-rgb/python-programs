# WAP to take a year and find whether it is leap year or not
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print("The year is a Leap Year")
else:
    print("The year is not a Leap Year")