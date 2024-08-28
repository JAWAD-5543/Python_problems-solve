# Write a program that calculates the factorial of a number
x=int(input("Enter factorial value! ="))
y=range(1,x+1)
z=1
for i in y:
    z*=i
print(z)
    