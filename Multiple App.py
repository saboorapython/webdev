print ("******Multiple App Payer*****")

select=int(input("Select an App you want to work: \n1, Calculator \n2. Student Marksheet \n3. Clothing Store \n4. Car Recommendation System"))

if select==1:
    name=input("Enter your name:")
    method=input("what your want to do? \n1. Addition \n2.subtraction \n3. Division \n4. Multiply")
    num1=eval(input("Enter number 1 to proceed:"))
    num2=eval(input("Entr number 2 to procees:"))
    if method=="1":
        print(f"This is your Addition:{num1+num2}")
    elif method=="2":
        print(f"This is your subtraction:{num1-num2}")
    elif method=="3":
        print(f"This is your Division:{num1/num2}")
    elif method=="4":
        print(f"This is your Multiply:{num1*num2}")    
    else:
        print("invalid input!")
if select==2:
    name=input("Enter your name:")
    eng=int(input("Enter your eng number:"))
    math=int(input("Enter your math number:"))
    phy=int(input("Enter your phy number:"))
    chem=int(input("Enter your chem number:"))
    urdu=int(input("Enter your urdu number:"))
    obtain=eng+math+phy+chem+urdu
    per=(obtain/500)*100
    if per>=70:
        print(f"Dear student {name}, \n{obtain}, \n{per} \nYour Grade:A")
    elif per>=60:
        print(f"Dear student {name}, \n{obtain}, \n{per} \nYour Grade:B")
    elif per>=50:
        print(f"Dear student {name}, \n{obtain}, \n{per} \nYour Grade:C")
    elif per>=40:
        print(f"Dear student {name}, \n{obtain}, \n{per} \nYour Grade:D")
    else:
        print("Grade: Pass")
if select==3:
    name=input("Enter your name:")
    budget=int(input("Enter your budget(Mnimumm spending limit 5000):"))       
if budget < 5000 and budget>=2000:
    print(f"Dear {name}, as per as your budget: that is {budget}, We recommended you for Casual wear")
elif budget>=5000 and budget<10000:
    print(f"Dear {name}, as per as your budget: that is {budget}, We recommended you for semi-casual wear")
elif budget>=10000 and budget<20000:
    print(f"Dear {name}, as per as your budget: that is {budget}, We recommended you for party wear")
elif budget>=20000 and budget<30000:
    print(f"Dear {name}, as per as your budget: that is {budget}, We recommended you for semi-formal wear")
elif budget>=30000 and budget<40000:
    print(f"Dear {name}, as per as your budget: that is {budget}, We recommended you for a formal category along with and all kind of wear")
else:
     print(f"Dear {name}, as per as your budget: that is {budget}, we recommended you to go home!")
     
if select==4:
    name=input("Enter your name:")
    budget=int(input("Enter your budget for ex:(\n1. 1000000-3000000, \n2.3000000-6000000, \n3.6000000-6500000, \n4.6500000-7000000"))
    cartype=input("Enter a sev/sedan you want?for ex:(jeep like, uplif cars, seden, corolla etc)")
    cc=int(input("Enter in cc in car you want? for ex:(1000-2000, 2000-3000, 3000-4000, 4000-5000)"))
    sitting=int(input("Enter your sitting capacity in car? for ex:(2,4,6,8)"))
    gear=input("Enter your gear auto/manual in car")
    
if (budget>=1000000 and budget<3000000) and (cartype=="suv") and (cc>=1000 and cc<=2000) and (sitting==2) and (gear==auto):
    print(f"Dear {name}, as per your requirements, you will have these cars under specific budget n\1.suv (Rs.1000000) \n2.sedan (Rs.3000000)")
elif (budget>=3000000 and budget<6000000) and (cartype=="suv") and (cc>=2000 and cc<=3000) and (sitting==4) and (gear==auto):
    print(f"Dear {name}, as per your requirements, you will have these cars under specific budget n\1.suv (Rs.3000000) \n2.sedan (Rs.6000000)")    
elif (budget>=6000000 and budget<6500000) and (cartype=="suv") and (cc>=3000 and cc<=4000) and (sitting==6) and (gear==auto):
    print(f"Dear {name}, as per your requirements, you will have these cars under specific budget n\1.suv (Rs.6000000) \n2.sedan (Rs.6500000)")    
elif (budget>=6500000 and budget<7000000) and (cartype=="suv") and (cc>=4000 and cc<=5000) and (sitting==8) and (gear==auto):
    print(f"Dear {name}, as per your requirements, you will have these cars under specific budget n\1.suv (Rs.6500000) \n2.sedan (Rs.7000000)")    
else:
    print(f"Dear {name}, as per your budget: that is {budget}, car not avaliable this budget!")

else:
    print("invalid input")