# Write a program that calculates the grade based on a given percentage.
result=int(input("Enter the percentage ="))
if result<=100 and result>=80:
    print("Result = A+")
elif result<80 and result>=70:    
    print("Result = A")
elif result<70 and result>=65:
    print("Result = A(-)")
elif result<65 and result>=60:
    print("Result = B")
elif result<60 and result>=55:
    print("Result = B(-)")
elif result<55 and result>=50:
    print("Result = C")
elif result<50 and result>=45:
    print("Result = D")
else:
    print("Result = F (Fail)")