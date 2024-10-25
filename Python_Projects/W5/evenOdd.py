n=int(input("Enter Num of Elements"))
lst=[]
even=[]
odd=[]

for i in range(n):
    lst.append(int(input("Enter Element: ")))

for i in lst:
    if i%2==0 :
        even.append(i)
    else:
        odd.append(i)

print("Even: ",even)
print("Odd: ",odd)

