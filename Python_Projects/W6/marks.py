students={"Rohan": 85, "Spoorthi": 90, "Aditi": 78, "Tanya": 92}

print("average marks for the class")
print(sum(students.values())/len(students))

name=input("Enter name of the student to be added to the record: ")
marks=int(input(f"Enter the marks secured by {name}: "))
students[name]=marks


max_marks=max(students.values())

for i,j in students.items():
    if(j==max_marks):
        print(f"Student {i} has got the highest marks securing {j}")