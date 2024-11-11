#lst={"name":{item:price},"name":{item:price}}
lst={"Rahul":{"egg":14,"chips":30,"Hand-sanitizer":55},
     "Sam":{"milk":22,"Biscuits":30,"egg":14}
     }

final_lst=set()

for i in lst.keys():
    for j in lst[i].items():
        final_lst.add(j)

final_lst=dict(final_lst)
bill_amt=sum(final_lst.values())

print("The final List ",final_lst.keys())
print("Final Amount to be paid: ",bill_amt)