n=int(input("Enter Num: "))
lst=[]

for i in range(1,n+1):
    k=[]
    for j in range(1,n+1):
        k.append(i*j)
    lst.append(k)

for i in lst:
    for j in i:
        print(j," ",end="")
    print()
