
decision in python (bit complex,and logical)
different scenarios
 
student Eligibility system!
marks=int(input("Enter Total Marks:"))
att=int(input("Enter attandance in %:"))
quiz=int(input("Enter Quiz Marks:"))
assignment=int(input("Enter Assignment Marks:"))
mid=int(input("Enter Mid Marks:"))
final=int(input("Enter Final Marks:"))
 
if (marks >=80 and marks<100) and att >=85 and quiz >=7 and assignment >=7 and mid>=25 and final>=45:
    print("Excellent Performance - Eligible for 100% Scholarship")
elif (marks >=80 and marks<100) and att >=80 and quiz >=6 and assignment >=6 and mid>=20 and final>=40:
    print("Best Excellent Performance - Eligible for 90% Scholarship")
elif (marks >=80 and marks<100) and att >=70 and quiz >=5 and assignment >=5 and mid>=15 and final>=35:
    print("Very Good Excellent Performance - Eligible for 70% Scholarship")
elif (marks >=80 and marks<100) and att <70:
    print("Average - Not Eligible for 70% Scholarship and in Warnings of SOA")
     
else:
    print("Not Allowed to sit in exams!")



User Name and Password
multiuser verification system:
name=input("Enter Your Name:")
wholenumber=int(input("Enter whole number:"))
decimal=float(input("Enter Decimal Number:"))
  
print(name, wholenumber,decimal)


a=eval(input("Enter any value:"))
print("The Data type of a value is :", type(a),"\nand the Value is:",a)
 




uname=input("Enter your user Name:").lower()
password=input("Enter your Password:")
 
if (uname=="saba" or uname=="sabakhan345@gmail.com" or uname=="03002287958") and (password=="Admin123"):
    print(f"Dear {uname}, welcome to the portal")
elif (uname=="miraha" or uname=="mirha129@gmail.com" or uname=="030912674832") and (password=="mirha678"):
    print(f"Dear {uname}, welcome to the portal")   
elif (uname=="saboora" or uname=="saboora786@gmail.com" or uname=="03128954367") and (password=="dell!2678"):
    print(f"Dear {uname}, welcome to the portal")   
elif (uname=="khan" or uname=="khan129@gmail.com" or uname=="030781690151") and (password=="1298Osbha"):
    print(f"Dear {uname}, welcome to the portal")   
else:
    print("Invalid User")
    
    




uname=input("Enter your user Name:").lower()
password=input("Enter your Password:")
domain=input("Enter your domain name:")
 
if (uname=="saba" or uname=="sabakhan345@gmail.com" or uname=="03002287958") and (password=="Admin123") and (domain=="Netfilx"):
    print(f"Dear {uname}, welcome to the Netfilx") 
elif (uname=="saboora" or uname=="saboora786@gmail.com" or uname=="03128954367") and (password=="dell!2678") and (domain=="linkedin"):
    print(f"Dear {uname}, welcome to the linkedin")
elif (uname=="khan" or uname=="khan129@gmail.com" or uname=="030781690151") and (password=="1298Osbha") and (domain=="Instagram"):
    print(f"Dear {uname}, welcome to the Instagram")
