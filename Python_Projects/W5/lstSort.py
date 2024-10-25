n=int(input("Enter Num of Elements"))
lst=[]


for i in range(n):
    lst.append(input("Enter Element: "))

lst2=sorted(lst)

if(lst==lst2):
    print("List is Already Sorted")
else:
    print("Sorted List")
    print(lst2)

