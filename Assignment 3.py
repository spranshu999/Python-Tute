
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
sample_number = int(input("Enter a number: "))
print(f" The factorial of the {sample_number} is: {factorial(sample_number)}")


""" Assignment 3 part 2"""
import math

num = float(input("Enter a number: "))
sqrt_result = math.sqrt(num)
print(f"The square root of {num} is {sqrt_result}")
if num >0:
    log_result = math.log(num)
    print(f"The logarithm of {num} is {log_result}")
else:
    print("Natural logarithm is undefined for zero or negative numbers.")
sine_result = math.sin(num)
print(f"The sine of {num} (in radian) is {sine_result}")
