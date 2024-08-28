# Write a program that finds the greatest common divisor (GCD) of two numbers.
num1=int(input("Enter the 1st Number ="))
num2=int(input("Enter the 2nd Number ="))
while num2>0:
    rem=num1%num2
    num1=num2
    num2=rem
print(f"GCD is = {num1}")    