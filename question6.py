# ### Problem 6:
# Create a function that will have the string firstName as a parameter. In the function ask the user for their last name. Print "Hello [FIRST & LAST NAME]" in the function. Call that function

def nameFunction(firstName):
    userLastName = input("Enter your last name ")
    print(f"Hello {firstName} {userLastName}")

nameFunction("Kenn")