s=input("Enter String").lower()
freq={}

for i in s:
    if i.isalpha():
        if i in freq.keys():
            freq[i]+=1
        else:
            freq[i]=1
        

for i in s:
    if (i==" "):
        continue
    if(freq[i]==1):
        print(f"{i} is the first non repeating character")
        break
else:
    print("NO NON repeating character found")