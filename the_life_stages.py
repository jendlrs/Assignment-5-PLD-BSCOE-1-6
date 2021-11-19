#Program 3: Life stages
#Create a program that ask for an age of a person
#Display the life stage of the person.
#Rules:
#0 - 12 : Kid
#13 - 17 : Teen
#18 : Debut
#19 above : Adult

print("\nWelcome! This program will tell you what phase of life you are in the present.")
name_= input("\nWhat is your name? ")
#Step 1: ask for an age of the person
def getAge():
    while True:
        try:
            age_= int(input("\nHow old are you? "))
            #Step 2: test if kid
            if age_ >=0 and age_ <=12:
                print(f"\nHi, {name_}! Because you are {age_} years old, you are still a Kid.\n")
            #Step 3: test if teen
            elif age_ >=13 and age_ <=17:
                print(f"\nHi, {name_}! Because you are {age_} years old, you are now a Teen.\n")
            #Step 4: test if debut
            elif age_ == 18:
                print(f"\nHi, {name_}! Because you are {age_} years old, you are a Debutant.\n")
            #Step 5: test if adult
            elif age_ >=19:
                print(f"\nHi, {name_}! Because you are {age_} years old, you are an Adult.\n")
            else:
                print("\nThere is no such age in negative numbers. Please try again.")
                continue
            break
        except ValueError:
            print("\nThe age you have entered is invalid. Please enter your age in numbers")
        continue

age= getAge()


