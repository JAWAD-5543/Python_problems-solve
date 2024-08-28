# Write a program that checks if a given number is prime or not.
value=int(input("Enter a number ="))
x=range(2,value)
for i in x:
    if value%i==0:
        print(f"{value} is not a Prime Number")
        break
else:
    print(f"{value} is a Prime Number")