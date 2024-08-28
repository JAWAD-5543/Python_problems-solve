#Write a program that reverses a given number.
n=int(input("Enter any number ="))
m=0
while n>0:
    r=n%10
    m=m*10+r
    n=n//10
print(f"Reverse number is ={m}")