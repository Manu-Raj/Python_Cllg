lst=[1,1,3,2,1,1,2,1,3,2]
freq=dict()
ans_lst=[]

for i in lst:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

sorted_lst_freq=sorted(freq.values())
for x in sorted_lst_freq:
    for k,v in freq.items():
        if(v==x):
            for i in range(x):
                ans_lst.append(k)
 
print(ans_lst)