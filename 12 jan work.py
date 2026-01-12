

print ("*****marksheet*****")
name=input("Enter you Full name:")
rollnumber=int(input("Enter your roll number:"))
eng=int(input("Enter your english number:"))
math=int(input("Enter your maths number:"))
phycis=int(input("Enter your phycis number:"))
isl=int(input("Enter your isl number:"))
chem=int(input("Enter your chem number:"))
obtain=eng+math+phycis+isl+chem
total=500
per= (obtain/total)*100

if per>=70:
    print(f"Dear student {name}, \n{rollnumber}, \n{obtain}, \n{total},  \n{per} \nYour Grade:A")
elif per>=60:
    print(f"Dear student {name}, \n{rollnumber}, \n{obtain}, \n{total},  \n{per} \nYour Grade:B")
elif per>=50:
        print(f"Dear student {name}, \n{rollnumber}, \n{obtain}, \n{total}, \n{per} \nYour Grade:C")
elif per>=40:
        print(f"Dear student {name}, \n{rollnumber}, \n{obtain}, \n{total}, \n{per}  \nYour Grade:D")
else:print("Grade: Pass")

