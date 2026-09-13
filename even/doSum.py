# WAP to define a method dosum() with parameter num to find sum of digits of a number
def dosum(num):    
    sum = 0
    while num > 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10
    return sum
n = int(input("Enter a number: "))
print("Sum of digits =", dosum(n))