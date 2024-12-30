def area_of_cirlce(radius):
    area=3.14*radius**2
    return area
def perimeter_of_circle(radius):
    perimeter=2*3.14*radius
    return perimeter
a=float(input("enter the radius: "))
print(f"area of circle is {area_of_cirlce(a)} and perimeter of circle is {perimeter_of_circle(a)}")