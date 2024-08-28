#Write a program that determines if a year is a leap year or not.
year=int(input("Enter any YEAR ="))
if year%4==0 and year%100!=0:
    print(f"This {year} year is LEAP YEAR ")
elif year%100==0 and year%400==0:
    print(f"This {year} year is LEAP YEAR ")
else:
    print(f"This {year} year is NOT a LEAP YEAR ")