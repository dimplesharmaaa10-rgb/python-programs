# WAP to define a method factorial that takes one parameter and returns factorial of given numbe
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact
n = int(input("Enter a number: "))
print("Factorial =", factorial(n))