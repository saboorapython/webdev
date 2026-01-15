#nested decision in python

print("*****Welcome to Weekend Planner*****")

mood=input("Enter your mood (happy/sad/tried):").lower()
budget=int(input("Enter your budget ($):"))
weather=input("Weather today? (sunday/rainy/cold):").lower()
company=input("who are you with?(alone/friends/family):").lower()

print("\n Planning Weekend..\n")

if mood=="happy":
    if budget> 1000:
        if weather == "sunny":
            if company == "friends":
                print(f"Dear {name}, For an Outdoor movie + street food party!")
            else:
                print("Watch Block buster Movie!")
        else:
            print("Order Pizza + Netflix at home")
    else:
        print("Watch Comedy movie on mobile with snacks!!!")
elif mood=="sad":
    if company=="alone":
        print ("Watch Motivational Movie and Order comfort food!")
    else:
        if budget >=500:
            print("Ice-Cream + Feel-good movie with loved ones!")
        else:
            print("Team + old classic Movie!")
elif mood=="tired":
    if weather == "cold":
        print("Sleep Early + Light Music!")
    else:
        if budget >300:
            print("Fast food + And watch comedy show!")
        else:
            print("Relax with music or book!")

else:
    print("Mood not recognized. Just relax and enjoy you time!")
            