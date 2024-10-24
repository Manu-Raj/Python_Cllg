attendence_Rec=[("A","P"),("B","A"),("C","P"),("D","A"),
                ("E","P"),("F","P"),("G","A"),("H","P"),
                ("I","P"),("J","P")]

prst=0
abb=0

for i in attendence_Rec:
    if i[1]=="P":
        prst+=1
    else:
        abb+=1

print("Present: ",prst)
print("Absent: ",abb)

s_name=input("Enter Name of Student to Chk attendence: ")
s_attd=input("Enter P or A: ")

for i in range(len(attendence_Rec)-1):
    if attendence_Rec[i][0]==s_name:
        if attendence_Rec[i][1]==s_attd:
            print("Attendence Record is Correct")
        else:
            attendence_Rec.remove(attendence_Rec[i])
            attendence_Rec.insert(i,(s_name,s_attd))
            print("Updated")
    
print(attendence_Rec)

new_name=input("Enter Name of Student to add to Reccord: ")

attendence_Rec.append((new_name,""))
print(attendence_Rec)

