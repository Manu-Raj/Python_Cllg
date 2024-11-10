e1={1,2,3,4,5}
e2={4,5,6,7,8,9}

print("Students who participated in both Events")
print(e1.intersection(e2))

print("Students who participated in only one of the events")
print(e1.symmetric_difference(e2))

print("Students who participated in atleast one event")
print(e1|e2)
