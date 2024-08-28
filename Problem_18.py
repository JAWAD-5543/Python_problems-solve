#Write a program that checks if a given string, is a palindrome.
str=str(input("Enter a string ="))
rev=str[::-1]
print(rev)
if str==rev:
    print(f"{str} is a PALINDROM ")
else:
    print(f"{str} is Not a PALINDROM")


