#Program 2: Find the lowest number
#Create a program that ask 3 numbers. 
#Find the lowest number using only if-else statement.
#Display the lowest number
print("\nThis program will tell you the lowest number you have entered.\n")

#Step 1: ask for 3 numbers convert, and store

def getnumbers():
    firstN= float(input("Enter first number: "))
    secondN= float(input("Enter second number: "))
    thirdN= float(input ("Enter third number: "))
    return firstN, secondN, thirdN
#Step 2: test the 3 numbers to find the lowest number

def lowestN(firstNA,secondNA,thirdNA):
    if firstNA < secondNA and firstNA <thirdNA:
        print(f"\nThe lowest number is {firstNA}\n")
    elif secondNA < firstNA and secondNA <thirdNA:
        print(f"\nThe lowest number is {secondNA}\n")
    elif thirdNA<firstNA and thirdNA <secondNA:
        print(f"\nThe lowest number is {thirdNA}\n")
        #This is for instances that the numbers entered are equal.
    else:
        if firstNA == secondNA and (firstNA and secondNA < thirdNA):
            print (f"\nThe lowest numbers are the first and second number which is {firstNA}.\n")
        elif firstNA == secondNA and (firstNA and secondNA > thirdNA):
            print (f"\nThe lowest number is {thirdNA}\n")
        elif firstNA == thirdNA and (firstNA and thirdNA <secondNA):
            print (f"\nThe lowest numbers are the first and third number which is {firstNA}.\n")
        elif firstNA == thirdNA and (firstNA and thirdNA >secondNA):
            print (f"\nThe lowest number is {secondNA}\n")
        elif secondNA== thirdNA and (secondNA and thirdNA <firstNA):
            print (f"\nThe lowest numbers are the second and third number which is {secondNA}.\n")
        elif secondNA == thirdNA and (secondNA and thirdNA > firstNA):
            print (f"\nThe lowest number is {firstNA}.\n")
        else:
            print("\nAll numbers you have entered are equal.\n")

first, second, third = getnumbers()
lowestN(first, second, third)