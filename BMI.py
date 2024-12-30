x=float(input("enter the weight: "))
y=float(input("enter the height: "))
z=x/y**2
if z<18.5:
    print("your BMI is:",z)
    print("you are underweight")
elif z>=18.5 and z<=24.9:
    print("your BMI is:",z)
    print("your BMI is normal")
elif z>=25 and z<=29.9:
    print("your BMI is:",z)
    print("you are overweight")
else:
    print("your BMI is",z)
    print("you are obese")