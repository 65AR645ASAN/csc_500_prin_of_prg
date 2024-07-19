#------------------------------------------------
# Name: Aditya Sandhu
# Course: CSC500-1 [Principles of Programming]
# Module: 1
#------------------------------------------------
# Part 1:
# Addition and Subtraction Program
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum_result = num1 + num2
sub_result = num1 - num2
print(f"The sum of {num1} and {num2} is: {sum_result}")
print(f"The difference of {num1} and {num2} is: {sub_result}")
# Part 2:
# Multiplication and Division Program
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
mul_result = num1 * num2
if num2 != 0:
    div_result = num1 / num2
else:
    div_result = "undefined (cannot divide by zero)"
print(f"The product of {num1} and {num2} is: {mul_result}")
print(f"The division of {num1} by {num2} is: {div_result}")
