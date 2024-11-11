s1=input("Enter first word: ")
s2=input("Enter second word: ")

s1=sorted(list(s1.lower().replace(" ","")))
s2=sorted(list(s2.lower().replace(" ","")))

for i in range(max(len(s1),len(s2))):
    if (s1[i]==s2[i]):
        continue
    else:
        print("NOT AN ANAGRAM")
        break
else:
    print("IS AN ANAGRAM")