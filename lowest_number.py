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
    elif thirdNA<firstNA and thirdNA <secondNA:
        print(f"The lowest number is {thirdNA}")
        #This is for instances that the numbers entered are equal.
    else:
        if firstNA == secondNA and (firstNA and secondNA < thirdNA):
            print (f"The lowest numbers are the first and second number which is {firstNA}")
        elif firstNA == secondNA and (firstNA and secondNA > thirdNA):
            print (f"The lowest number is {thirdNA}")
        elif firstNA == thirdNA and (firstNA and thirdNA <secondNA):
            print (f"The lowest numbers are the first and third number which is {firstNA}.")
        elif firstNA == thirdNA and (firstNA and thirdNA >secondNA):
            print (f"The lowest number is {secondNA}")
        else:
            print("To be updated")


first, second, third = getnumbers()
lowestN(first, second, third)