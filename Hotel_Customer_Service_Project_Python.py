# Task 1
customer = "Y"
Grand_Total = 0

while( customer == "Y" or customer == "Y"):
    print("*********WELCOME To Hotel OASIS*********")
    print(f"")
    print(f"")
    a = [["French Fries",2.0,"01"],["1/4 pound burger",5.0,"02"],["1/4 pound cheese burger",5.55,"03"],
         ["1/2 pound burger",7.0,"04"],["1/2 pound cheese burger",7.5,"05"],["medium pizza",9.0,"06"],
         [" medium pizza with extra toppings",11.0,"07"],["large pizza",12.0,"08"],
         [" large pizza with extra toppings",14.5,"09"],[" garlic bread",4.5,"10"]]
    i = 0
    for i in range(len(a)):
        print("************************************************")
        print(f"")
        print(f"Item:{a[i][0]} Price:{a[i][1]}$ Item code:{a[i][2]}")
        print(f"")
    
    print("************************************************")
    
    print("*********Below is the Discount chart*********")
    print(" Bill<500                   No Discount  ")
    print(" Bill>500 and <800          10% Discount  ")
    print(" Bill>800 and <1200         15% Discount  ")
    print(" Bill>1200 and <1500        20% Discount  ")
    print(" Bill>1500                  25% Discount  ")
    
    print("************************************************")
    
    
    
    # Task 2
    a = [["French Fries",2.0,"01"],["1/4 pound burger",5.0,"02"],["1/4 pound cheese burger",5.55,"03"],
         ["1/2 pound burger",7.0,"04"],["1/2 pound cheese burger",7.5,"05"],["medium pizza",9.0,"06"],
         ["medium pizza with extra toppings",11.0,"07"],["large pizza",12.0,"08"],
         ["large pizza with extra toppings",14.5,"09"],["garlic bread",4.5,"10"]]
    i = 0
    amt = 0
    ord_code = 0
    quan = 0
    response = "Y"
    totalL = []
    itemL = []
    amtL = []
    quanL = []
    L = []
    itemname = ""
    T = []
    x = 0
    
    while(response == "Y" or response == "y"):
        ord_code = input("Enter the order code:")
    
        while( not ord_code.isdigit() or int(ord_code) > 10 or len(ord_code) > 2) :   
            ord_code = input("INVALID! please enter the correct order code between 01 to 10:")
        
        if ord_code == "1":
                ord_code = "01"       
        if ord_code == "2":
                ord_code = "02"
        if ord_code == "3":
                ord_code = "03"
        if ord_code == "4":
                ord_code = "04"
        if ord_code == "5":
                ord_code = "05"
        if ord_code == "6":
                ord_code = "06"
        if ord_code == "7":
                ord_code = "07"
        if ord_code == "8":
                ord_code = "08"
        if ord_code == "9":
                ord_code = "09"
       
        quan = input("Enter the quantity:")
        while( not quan.isdigit()):
               quan = input("INVALID! Please Enter the correct quantity:")
        quan=int(quan)
        
        for i in range(len(a)):
                if a[i][2] == ord_code:
                    amt = a[i][1]
                    itemname = a[i][0]
    
        ord_total = quan*amt     
        itemL.insert(x,itemname)
        amtL.insert(x,amt)
        quanL.insert(x,quan)
        totalL.insert(x,ord_total)     
        
        itemL.extend(amtL)
        itemL.extend(quanL)
        itemL.extend(totalL)  
    
        T = itemL.copy()
    
        L.append(T)
        x = x+1
        
        
        itemL.clear()
        amtL.clear()
        quanL.clear()
        totalL.clear()
    
        
        response = input("Do you want to order something else? (Y/N):")
        
        while(response.lower() not in ["y","n"]):
            response = input("INVALID Response! Please enter correct response (Y/N):")
        while(response.upper() not in ["Y","N"]):  
            response = input("INVALID Response! Please enter correct response (Y/N):")
          
            
             
    if response == "N" or response == "n":
        print(f"******************************Invoice************************************************")
        print(f"")
        import random
        q = random.randint(0, 99999)
        print(f"Invoice number:{q}")
        
        print("{: <35s}{: <10s}{: <10s}{: <10s}".format("Item name"," | Price per Item"," | Quantity"," | Total Price"))
        i = 0   
        billtotal = 0
        for i in range(len(L)):   
            print("{: <42s}{: <18s}{: <11s}{: <3s}".format(f"{L[i][0]}",f"{L[i][1]}",f"{L[i][2]}",f"{L[i][3]}"))
     
            billtotal = billtotal + L[i][3]
        print(f"                                                          Total Bill:{billtotal}$ ")
    
        if billtotal < 500:
            aftdis = billtotal
            p = 0
        elif billtotal > 500 and billtotal < 800:
            aftdis = billtotal/100*10
            p = 10
            billtotal = billtotal - aftdis
            
        elif billtotal > 800 and billtotal < 1200: 
            aftdis = billtotal/100*15
            p = 15
            billtotal = billtotal - aftdis
            
        elif billtotal > 1200 and billtotal < 1500: 
            aftdis = billtotal/100*20
            p = 20
            billtotal = billtotal - aftdis
            
        elif billtotal > 1500 : 
            aftdis = billtotal/100*25
            p = 25
            billtotal = billtotal - aftdis        
                                                  
        print(f"                                                          After ({p}%) Discount: {round(billtotal,2)}$                      ")                                                                   
        print("*******************************************************************************************")
        print(f" Your payment due is : {round(billtotal,2)}$ ")
                                        
    # Task 3
    change = 0
    
    b = input("Enter the amount of money that you will pay:")
    
    while(isinstance(b, float) == True) or (b.isalpha() == True):   
            b = input("INVALID! please enter the correct amount:")
    b = float(b)
    while(b < billtotal ):
          b = float(input(f" Your due is {billtotal}$ and the amount given by you is less than this:"))
    while(b >= billtotal):
        print(f"")
        print("**********Thanks for Payment**********") 
        
        change = float(b) - float(billtotal)
        
        print(f" change returned: {round(change,2)}$")
        break
        print(f"")
    print(f"**********Welcome to our Rating Center!**********")
    y = input("You can rate from 0-5 0 meaning worst and 5 meaning best:")
    while( not y.isdigit() or int(y) > 5 ): 
                  print(f"")
                  print(f"")
                  y = input("Please enter a valid rating from 0-5:") 
    if int(y) == 0:
                  print(f"")
                  print(f"We ard you feel this way") 
    elif int(y) == 1:
                  print(f"We are sad you feel this way")   
    elif int(y) == 2:
                  print(f"")
                  print(f"We are somewhat sad you feel this way")
    elif int(y) == 3:
                  print(f"")
                  print(f"We are fine you feel this way! If you would like to,feel free to jump by later")
    elif int(y) == 4:
                  print(f"")
                  print(f"We are happy you feel this way! feel free to jump by later") 
    elif int(y) == 5:
                  print(f"")
                  print(f"We are glad you feel this way! feel free to jump by later")
                  print(f"")
    else:
                  print(f"")
              
   
    Grand_Total = Grand_Total + billtotal 
    customer = input("Is there any more customers (Y/N):")
    print(f"")
    if customer == "N" or customer == "n":
        print(f"**********DAILY RECORD********************")
        print(f" Today's Total Sales : {Grand_Total}")
        print(f" Today's Total Profit: {round(Grand_Total/100*10,2)}")
        print(f"******************************************")
     
        






