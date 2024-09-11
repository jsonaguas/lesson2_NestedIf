#Task 1
#You should change the input type to an integer. 
attendees = int(input("Enter number of attendees: "))
venue = ("large hall") if attendees >= 100 else ("conference room")
audio_system = ("PA system") if attendees >= 100 else ("microphone")
print("Book " + venue + "and " + audio_system)


#Task 3
food_choice = input("Vegetarian meal: Yes or No? ")
if food_choice.lower() == "yes":
    print("Recommend Veggie Delight Caterers")
else:
    print("Recommend Gourmet Meals Caterers")
                    