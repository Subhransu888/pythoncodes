a=float(input("enter the 1st number: "))
b=float(input("enter the 2nd number: "))
c=input("enter the operation you want to perform(+,-,/,*): ")
if c=='+':
    print("addition of two numbers is: ",a+b)
elif c=='-':
    print("subtraction of two numbers is: ",a-b)
elif c=='*':
    print("multiplication of two numbers is: ",a*b)
elif c=='/':
    print("division of two numbers is: ",a/b)
else:
    print("wrong operator choose the right one")