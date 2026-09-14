# consider the equation : 3x=5y+10 ... and 4x-2y=7 ... find the value of x and y using numpy package in python.
import numpy as np

# Coefficients matrix
A = np.array([[3, -5],
              [4, -2]])
# Constants vector
B = np.array([10, 7])
# Solve the system of equations
x, y = np.linalg.solve(A, B)
print("Value of x:", x)
print("Value of y:", y)
