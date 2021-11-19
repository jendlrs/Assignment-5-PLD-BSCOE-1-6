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
            age_= int(input("\nHow old are you? "))
            #Step 2: test if kid
            if age_ >=0 and age_ <=12:
                print(f"\nHi, user! Because you are {age_} years old, you are still a Kid.\n")
            else:
                print("Others")
            #Step 3: test if teen
            #Step 4: test if debut
            #Step 5: test if adult
            break
        except ValueError:
            print("\nThe age you have entered is invalid. Please enter your age in numbers")
            continue
    return age_

age= getAge()


