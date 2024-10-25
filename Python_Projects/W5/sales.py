sales_Rec=[25000,30000,7500,50350,-46555,12900,75000,96000,84525,65412,78545,33600,74525,68544,65421]

for i in sales_Rec:
    if i<0:
        sales_Rec.remove(i)

print("The Average sales",(sum(sales_Rec)/len(sales_Rec)))
print("Maximum Sales on day ",sales_Rec.index(max(sales_Rec))+1)
print("Minimum Sales on day ",sales_Rec.index(min(sales_Rec))+1)

