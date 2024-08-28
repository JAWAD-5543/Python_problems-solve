#Write a program that finds the maximum of three numbers
x=int(input("Enter 1st numbers ="))
y=int(input("Enter 2nd numbers ="))
z=int(input("Enter 3rd numbers ="))
if x>y and x>z:
    print(f"1st number {x} is the maximum number")
elif y>x and y>z:
    print(f"2nd number {y} is the maximum number")
else:
    print(f"3rd number {z} is the maximum number")