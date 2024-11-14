import csv
f=open('feedback.txt','r')
f2=open('good_feedback.txt','w+')
f3=open('Bad_feedback.txt','w+')

good=['good','excellent','positive','great','happy']
bad=[ "poor", "bad", "disappointed", "unsatisfied."]
good_d=dict()
bad_d=dict()
gl=0
bl=0

data=f.read().split(".")

for i in data:
    for j in i.split():
        if j in good:
            f2.write(i)
            gl+=1
            if j in good_d.keys():
                good_d[j]+=1
            else:
                good_d[j]=1
        elif j in bad:
            f3.write(i)
            bl+=1
            if j in bad_d.keys():
                bad_d[j]+=1
            else:
                bad_d[j]=1

print(good_d)
print(bad_d)

f_csv=open('keyword_counts.csv','w+')
write=csv.writer(f_csv)
write.writerow(['feedback',"num of lines "])
write.writerows([['Good',gl],['Bad',bl]])

f.close()
f2.close()
f3.close()
f_csv.close()
