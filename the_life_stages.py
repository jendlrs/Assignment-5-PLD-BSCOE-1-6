#Program 3: Life stages
#Create a program that ask for an age of a person
#Display the life stage of the person.
#Rules:
#0 - 12 : Kid
#13 - 17 : Teen
#18 : Debut
#19 above : Adult

#Step 1: ask for an age of the person
def getAge():
    while True:
        try:
            age_= int(input("How old are you? "))
            break
        except ValueError:
            print("The age you have entered is invalid. Please enter your age in numbers")
            continue
    return age_

age= getAge()
#Step 2: test if kid
#Step 3: test if teen
#Step 4: test if debut
#test if adult

