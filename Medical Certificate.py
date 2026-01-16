# Scenario-Based Programming Questions (Nested If-Else)

name=input("Enter Name:")
tclss=int(input("Enter a Number of total classes:"))
clss=int(input("Enter a number of class attanded:(in No(s)):"))
med_c=int(input("Do you have Medical certificate?: \Press 1. for Yes  \nPress 2. for No:"))

print("\n Medical Certificate....\n")

per=(clss/tclss)*100

if per>=75:
    print("You are Allowed to sit in exam! No Medical")
elif per<75:
    print(f"Dear {name} Your Percentage is below 75%")
    med_c=int(input("Do you have Medical Certificate?: \Press 1. for Yes \Press2. for No \n:"))
    if med_c==1:
        print("Your medical certificate is processed for verification:")
        ver=int(input("Let me know is it signed and stampped? : \nPress 1. for Yes \nPress 2. for No:"))
        if ver==1:
            print("Dear {name}, Despit your Attandance is low, but your Medical Certificate is verified and your're Allowed to sit in exam")
        elif ver==2:
            print("Dear {name}, Despit your Attandance is low and your Medical Certificate is Not verified and your're Not Allowed to sit in exam")
        else:
            print ("Invalid inut")           
    else:
        print("Your are No Allowed to sit in exam!")
else:
    print("Invalid input, Restart the application!")
            
    
