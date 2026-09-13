# WAP to define a method isprime() with parameter num to check whether the number is prime or not
def isprime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
n = int(input("Enter a number: "))
if isprime(n) == True :
    print("Prime Number")
else:
    print("Not a Prime Number")