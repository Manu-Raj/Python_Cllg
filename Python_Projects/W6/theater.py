#theater={"Movie_name":{Seat_num:Person_name}}
theater=dict()


#data=["name","movie_name","seat num"]
while True:
    dat=input("Enter Name-Movie_name-Seat_number to book or Exit ")
    if(dat in ("EXIT","Exit","exit")):
        break

    dat=dat.split("-")

    if(dat[1]  not in theater.keys()):
        theater[dat[1]]={dat[2]:dat[0]}        
    else:
        if(dat[2] in theater[dat[1]].keys()):
            print("Seat taken Try again")
        else:
            theater[dat[1]][dat[2]]=dat[0]
        

print(theater)
