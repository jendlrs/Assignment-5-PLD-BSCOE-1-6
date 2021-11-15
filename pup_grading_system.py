#Program 1: PUP Grading System
#Section 8 of https://www.pup.edu.ph/studentservices/files/ThePUPStudentHandbook2014.pdf
   
    # grade/mark   Percentage      Description
    # 1.0           97-100          Excellent
    # 1.25          94-96           Excellent
    # 1.5           91-93           Very Good
    # 1.75          88-90           Very Good
    # 2.0           85-87           Good
    # 2.25          82-84           Good
    # 2.5           79-81           Satisfactory
    # 2.75          76-78           Satisfactory
    # 3.0           75              Passing
    # 5.0           65-74           Failure
    # Inc.                          Incomplete
    # W                             Withdrawn
    # D                             Dropped

#Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
#Example:
#Input grade: 87.6
#Grade/Mark: 1.75
#Description: Very Good

#Step 1: ask for student grade in percentage, convert, and store
# Can round off grades
#print("Please enter your grade percentage. Type N if you do not have grade percentage attained.\n")
#quest_grade= input("Answer:  ")from pup import roundOffGrade_


print("Please enter your grade percentage here. Type 'N' if you do not attained any grade.")
while True:
    try:
        quest_grade= float(input("Answer:  ")) 
        roundOffGrade = round(quest_grade, 0)
        print(roundOffGrade)

#Step 2: test if 1.0 
        if roundOffGrade >=97 and roundOffGrade <=100:
            print("Grade mark: 1.00\nDesription: Excellent")
#Step 3: test if 1.25
        elif roundOffGrade >=94 and roundOffGrade <=96:
            print("Grade mark: 1.25\nDesription: Excellent")
#Step 4: test if 1.5
        elif roundOffGrade >=91 and roundOffGrade <=93:
            print("Grade mark: 1.50\nDesription: Very Good")
#Step 3: test if 1.75
        elif roundOffGrade >=88 and roundOffGrade <=90:
            print("Grade mark: 1.75\nDesription: Very Good")
#Step 4: test if 2.0
        elif roundOffGrade >=85 and roundOffGrade <=87:
            print("Grade mark: 2.00\nDesription: Good")
#Step 3: test if 2.25
        elif roundOffGrade >=82 and roundOffGrade <=84:
            print("Grade mark: 2.25\nDesription: Good")
#Step 4: test if 2.5
        elif roundOffGrade >=79 and roundOffGrade <=81:
            print("Grade mark: 2.5\nDesription: Satisfactory")
#Step 3: test if 2.75
        elif roundOffGrade >=76 and roundOffGrade <=78:
            print("Grade mark: 2.75\nDesription: Satisfactory")
#Step 4: test if 3.0
        elif roundOffGrade == 75:
            print("Grade mark: 3.00\nDesription: Passing")
#Step 5: test if 5.0
        elif roundOffGrade >=65 and roundOffGrade <=74:
            print("Grade mark: 5.00\nDesription: Failure")
#Step 6: test if incomplete, withdrawn, dropped 
        else:
            print("The grade you entered is invalid. Grade percentage must be in positive numbers.")
        break

    except ValueError:
        #The following questions is also connected to Section 8 "Grading System"
        
        print("Please answer the following questions to know if your status is Incomplete, Withdrawn or Dropped.")
        majorExam=input("1. Have you take your major exam?\nType Y if Yes and N if No: ")
        withdrawn= input ("2. Have you written a letter to withdraw your enrollment?\nType Y if Yes and N if No: ")
        absent= input ("3. Have you absent 10 times in the semester?\nType Y if Yes and N if No: ")
    
        if (majorExam== "N" and withdrawn == "N") and (absent=="N"):
            print("Grade Mark: Inc.\nDescription: Incomplete.\n")
        elif (majorExam== "Y") and (withdrawn == "N" or absent== "N"):
            print("It looks like there is a problem occured.\nPlease ask your teacher for clarification.")
        elif majorExam== "N" and withdrawn == "Y":
            print("Grade Mark: W\nDescription: Withdrawn\nA Withdrawn mark is given if the student voluntarily withdraws in writing from a subject\nat any time but not less than one (1) month before the final examination")
        else:    
            print("Grade Mark: D\nDescription: Dropped\nYour teacher gave you a dropped mark for exceeding\nthe allowable number of absences or for not attending class since the start of the term.")
        break
