s=input("Enter String")
ans=""

lst=list(s)

for i in range(len(s)-1,-1,-1):
    ans+=lst[i]

print(ans)