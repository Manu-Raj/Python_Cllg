s=input("Enter a Sentence: ")

v=0
c=0
for i in s:
    if i in " ":
        continue
    elif i in"AEIOUaeiou":
        v+=1
    else:
        c+=1

print(f"The sentence contains {v} Vowels")
print(f"The sentence contains {c} Consonants")

lst=s.split()
lens=[len(i) for i in lst]
print("Longest Word is: ",lst[lens.index(max(lens))])

#For the Reverse of the Sentence
for i in range(len(lst)-1,-1,-1):
    print(lst[i], end=" ")