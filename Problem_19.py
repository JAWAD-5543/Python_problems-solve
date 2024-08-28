# Write a program that generates a random number and allows the user to guess it.
import random
value=int(input("Enter any integer value in 1 to 10 ="))
a=random.randint(1,10)
if value==a:
    print(f"Your given value is match with the random value,Given value={value} & Random value={a}")
else:
    print(f"Your given value is NoT match with the random value,Given value={value} & Random value={a}")