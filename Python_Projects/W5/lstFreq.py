n=int(input("Enter Num of Elements"))
lst=[]


for i in range(n):
    lst.append(input("Enter Element: "))

least=[0,100]

for i in lst:
    if (lst.count(i)<least[1]):
        least[0]=i
        least[1]=lst.count(i)

print("The Element with least Frequency: ",least[0])
print("Having Freq: ",least[1])