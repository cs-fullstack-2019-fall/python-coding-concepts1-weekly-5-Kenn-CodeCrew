# ### Problem 2:
# Ask the user for a string. If they enter “Kenn”, “Kevin”, “Erin”, or “Autumn” print “Hello Teacher”. Otherwise print “Hello Student”

userInput = input("Enter a string")

if (userInput == "Kenn" or userInput == "Kevin" or userInput == "Erin" or userInput == "Autumn"):
    print("Hello Teacher")
else:
    print("Hello Student")
