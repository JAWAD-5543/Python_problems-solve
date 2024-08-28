#Write a program that prints the multiplication table of a given number.
value=int(input("Enter the value ="))
x=0
for i in range(1,11):
    x=value*i
    print(f"{value}*{i}={x}")