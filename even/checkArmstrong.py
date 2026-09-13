# WAP to define a method checkarmstrong() with parameter num that returns True if number is Armstrong else False
def checkarmstrong(num):
    original = num
    sum = 0
    digits = len(str(num))
    while num > 0:
        digit = num % 10
        sum = sum + (digit ** digits)
        num = num // 10
    if sum == original:
        return True
    else:
        return False
n = int(input("Enter a number: "))
if checkarmstrong(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")