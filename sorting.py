a=[]
n=int(input("enter number of elements in the list:"))
for i in range(n):
    element=int(input(f"enter the element {i+1}: "))
    a.append(element)
print(f"list is:{a}")
a.sort(reverse=True)
print(f"sorted list is:{a}")