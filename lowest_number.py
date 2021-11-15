#Program 2: Find the lowest number
#Create a program that ask 3 numbers. 
#Find the lowest number using only if-else statement.
#Display the lowest number

#Step 1: ask for 3 numbers convert, and store
def getnumbers():
    firstN= int(input("Enter first number: "))
    secondN= int(input("Enter second number: "))
    thirdN= int(input ("Enter third number: "))
    return firstN, secondN, thirdN
#Step 2: test the 3 numbers to find the lowest number


first, second, third = getnumbers()