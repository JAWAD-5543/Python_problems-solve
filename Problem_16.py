#Write a program that finds the sum of all even numbers between 1 and `n`.
n=int(input("Enter the value of 'n' ="))
count=1;sum=0
while count<=n:
    print(count)
    count+=1
    if count%2==0:
        sum+=count
print(f"Sum is = {sum}")