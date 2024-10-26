from datetime import datetime

#rec=[[(Vehicle, Reg),[Borrower_name, Phone_num],[Borrow_date, Expected return, rent, hourly_rent, deposit, in_hand]],[<for vehicle 2>]]
rec=[[("Car", 2478),["Alice", 975318642],["15/10/2024,10.30 AM", "18/10/2024,10.30 AM", 1000, 50, 1500, True]]]

options="1 Display Available vehicles \n 2 Display rent Details \n 3 Update Rent Details \n 4 Calculate rent \n 5 Return vehicle \n 6 Exit"
date_format ="%d/%m/%Y,%H.%M %p"


while True:
    print(options)
    ch=int(input("Enter Option: "))
    if(ch==1):
        flag=0
        for i,j,k in rec:
            if(k[5]==False):
                flag=1
                print("Vehicle Type: ",i[0])
                print("Vehicle Reg Num: ",i[1])
        if(flag==0):
            print("NO Vehicles Available for Rent ")

    elif(ch==2):
        num=int(input("Enter Vehicle Reg Num"))
        for i,j,k in rec:
            if(i[1]==num):
                print(f"Rent: {k[2]} per day")
                print(f"Extra Rent: {k[3]} per hour")
                print(f"Deposit: {k[4]}")

    elif(ch==3):
        num=int(input("Enter Vehicle Reg Num"))
        rent=int(input("Enter New Rent Value"))
        e_rent=int(input("Enter New Extra Rent Value"))
        dep=int(input("Enter New Deposit Value"))

        for i,j,k in rec:
            if(i[1]==num):
                j[2]=rent
                j[3]=e_rent
                j[4]=dep
                print("Updated Succesfully")
                break
        else:
            print("Vehicle Not Found")
            
    elif(ch==4):
        print("Calculating Rent based on Expected return")
        num=int(input("Enter Vehicle Reg Num"))

        for i,j,k in rec:
            if (i[1]==num):
                borr=datetime.strptime(k[0],date_format)
                exp_ret=datetime.strptime(k[1],date_format)
                print("Expected Amt: ",(exp_ret-borr).days*k[2])

    elif(ch==5):
        num=int(input("Enter Vehicle Reg Num"))
        

        now=datetime.now()
        now=now.strftime(date_format)

        for i,j,k in rec:
            if (i[1]==num):
                k[5]=False
                borr=datetime.strptime(k[0],date_format)
                exp_ret=datetime.strptime(k[1],date_format)
                if(k[1]==now):
                    t=datetime.strptime(now,date_format)-borr
                    print("Amt to be Paid: ",t.days*k[2])
                else:
                    t=exp_ret-borr
                    i_amt=t.days*k[2]+((datetime.strptime(now,date_format)-exp_ret).days*24)*k[3]
                    print("Expected Time Exceeded")
                    print("Amt to be Paid: ",i_amt)
                

    elif(ch==6):
        break
    else:
        print("Wrong Input given TRY Again")
    print()