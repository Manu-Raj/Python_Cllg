import csv 

key_f=open("output_key.txt","r")
key_ans=key_f.read().split("\n")

marks_alloted_f=open("marks_alloted.csv","w",newline="")
writer=csv.writer(marks_alloted_f)
writer.writerow(["Student","Marks Secured"])
lst=[]


#num of students n
n=10

for i in range(1,n+1):
    f=open(f"student_{i}.txt","r")
    student_ans=f.read().split("\n")
    marks=0

    for j in range(len(key_ans)):
        if(student_ans[j]==key_ans[j]):
            marks+=2

    lst.append([f"student_{i}",marks])
    f.close()


writer.writerows(lst)
print("Marks alloted and have been saved in marks_alloted.csv")
key_f.close()
marks_alloted_f.close()
