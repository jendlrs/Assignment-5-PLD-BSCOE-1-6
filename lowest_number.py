#Program 2: Find the lowest number
#Create a program that ask 3 numbers. 
#Find the lowest number using only if-else statement.
#Display the lowest number

#Step 1: ask for 3 numbers convert, and store
def getnumbers():
    firstN= float(input("Enter first number: "))
    secondN= float(input("Enter second number: "))
    thirdN= float(input ("Enter third number: "))
    return firstN, secondN, thirdN
#Step 2: test the 3 numbers to find the lowest number
def lowestN(firstNA,secondNA,thirdNA):
    if firstNA < secondNA and firstNA <thirdNA:
        print(f"The lowest number is {firstNA}")
    elif secondNA < firstNA and secondNA <thirdNA:
        print(f"The lowest number is {secondNA}")
    else:
        print(f"The lowest number is {thirdNA}")

first, second, third = getnumbers()
lowestN(first, second, third)