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
quest_grade= input("Do you have grade percentage attained? Yes or No: ")

if quest_grade== "Yes":
    grade_= float(input("Enter grade percentage: ")) 
    roundOffGrade = round (grade_)

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
        if roundOffGrade <=64 and roundOffGrade >0:
            print("It looks like the grade you entered do not meet the minimum grade percentage to either pass or have a failure mark.\nPlease answer the following questions to know if you are Incomplete, Withdrawn or Dropped.")
            majorExam=input("1. Have you take your major exam?\nType Y if Yes and N if No: ")
            withdrawn= input ("2. Have you written a letter to withdraw your enrollment?\nType Y if Yes and N if No: ")
            absent= input ("3. Have you absent 10 times in the semester?\nType Y if Yes and N if No: ")

            if (majorExam== "N" and withdrawn == "N") and (absent=="N"):
                print("Grade Mark: Inc.\nDescription: Incomplete")
            elif (majorExam== "Y") and (withdrawn == "N" or absent== "N"):
                print("It looks like there is a problem occured.\nPlease ask your teacher for clarification.")
            elif majorExam== "N" and withdrawn == "Y":
                print("Grade Mark: W\nDescription: Withdrawn")
            else:
                print("Grade Mark: D\nDescription: Dropped\nIt looks like your teacher gave you a dropped mark for exceeding\nthe allowable number of absences or for not attending class since the start of the term.")
        else:
            print("The grade you entered is invalid. Grade percentage must be in positive numbers.")
else:
    print("It looks like you don't have grades\nPlease answer the following questions to know if your status is Incomplete, Withdrawn or Dropped.")
    majorExam=input("1. Have you take your major exam?\nType Y if Yes and N if No: ")
    withdrawn= input ("2. Have you written a letter to withdraw your enrollment?\nType Y if Yes and N if No: ")
    absent= input ("3. Have you absent 10 times in the semester?\nType Y if Yes and N if No: ")
    
    if (majorExam== "N" and withdrawn == "N") and (absent=="N"):
        print("Grade Mark: Inc.\nDescription: Incomplete")
    elif (majorExam== "Y") and (withdrawn == "N" or absent== "N"):
        print("It looks like there is a problem occured.\nPlease ask your teacher for clarification.")
    elif majorExam== "N" and withdrawn == "Y":
        print("Grade Mark: W\nDescription: Withdrawn")
    else:    
        print("Grade Mark: D\nDescription: Dropped\nIt looks like your teacher gave you a dropped mark for exceeding\nthe allowable number of absences or for not attending class since the start of the term.")