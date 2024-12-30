grade=float(input("enter your grades (0.0 to 1.0): "))
if grade>=0.9 and grade<=1.0:
    print("grade-A")
elif grade>=0.8 and grade<0.9:
    print("grade-B")
elif grade>=0.7 and grade<0.8:
    print("grade-C")
elif grade>=0.6 and grade<0.7:
    print("grade-D")
elif grade<0.6:
    print("grade-F")
elif grade<0.0 or grade>1.0:
    print("grade shoud be between 0.0 to 1.0")