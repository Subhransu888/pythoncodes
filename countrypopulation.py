import matplotlib.pyplot as plt
a=["india","Bangladesh","Africa","China","America"]
b=[180,50,60,200,70]
plt.title("population of 5 diffrent countries")
plt.xlabel("name of countries")
plt.ylabel("population in crores")
plt.bar(a,b,color='g')
plt.show()
plt.plot(a,b)
plt.show()
plt.scatter(a,b)
plt.show()
plt.hist(b,bins=10,color='r')
plt.show()