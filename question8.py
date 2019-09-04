# ### Problem 8:
# Create a function that asks the user to enter a number. If the number is between and include -50 and 5, return "Funds too low". If the number is between 5 and 50, return “You should add more funds.” If the number is more than 50, return “Just enough.”

def fundsFuntion():
    userInput = int(input("Enter a number"))
    if(userInput>=-50 and userInput<=5):
        return("Funds too low")
    elif(userInput>5 and userInput<=50):
        return("You should add more funds")
    elif(userInput>50):
        return("Just enough")


print(fundsFuntion())