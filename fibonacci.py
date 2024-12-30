a=int(input("enter the limit: "))
b,c=0,1
count=0
while count<a:
    print(b,end=" ")
    b,c=c,b+c
    count+=1