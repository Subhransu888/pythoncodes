def count_string(string):
    count=0
    for i in string:
        if ('a'<=i<='z' or 'A'<=i<='Z'):
            count=count+1
    return count
string=input("enter a string: ")
count=count_string(string)
print("the number of letters in the string is:",count)