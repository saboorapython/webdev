#multipule condition ky lie python:(nested desicion)

#Nested Decision in python

print("****Welcoe to Netflix*****")

name=input("Enter your Name:")
email=input("Enter your Email:")
password=input("Enter your password:")
age=int(input("Enter your age:"))

if age>=18:
    print(f"Dear {name}, Welcome to Netflix!")
    if email=="maha347@gmail.com" and password=="Admin234":
        print(f"Dear {name}, Welcome to the Netflix Sessions, Please Select Category")
    elif email=="saba129@gmail.com" and password=="saba8765":
        print(f"Dear {name}, Welcome to the Netflix Sessions, Please Select Category")
    elif email=="fakhir654@gmail.com" and password=="fakhir8795":
        print(f"Dear {name}, Welcome to the Netflix Sessions, Please Select Category")
    elif email=="maha786@gmail.com" and password=="maha890":
        print(f"Dear {name}, Welcome to the Netflix Sessions, Please Select Category")    
    else:
        print(f"Dear {name}, Your Login Credentials are invalid!")
else:
    print(f"Dear {name}, Please watch pogo!")
    