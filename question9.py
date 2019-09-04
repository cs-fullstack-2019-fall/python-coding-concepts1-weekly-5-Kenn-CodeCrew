# ### Problem 9:
# Ask the user for a positive number. Create an empty array and starting from zero, add each number by 1 into the array. Print EACH ELEMENT of the array.

userInput = int(input("Enter a positive number"))
emptyArray = []

for index in range(userInput+1):
    emptyArray.append(index)

for eachElement in emptyArray:
    print(eachElement)