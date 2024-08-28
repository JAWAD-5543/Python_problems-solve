#Write a program that prints the first `n` natural numbers.
x=int(input("Enter the value of 'starting point' ="))
y=int(input("Enter the value of 'Ending point' ="))
z=range(x,y+1)
for i in z:
    print(i)