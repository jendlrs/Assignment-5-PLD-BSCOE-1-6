#Program 1: PUP Grading System
#Section 8 of https://www.pup.edu.ph/studentservices/files/ThePUPStudentHandbook2014.pdf
   
    # grade/mark   Percentage      Description
    # 1.0           97-100          Excellent
    # 1.25          94-96           Excellent
    # 1.5           91-93           Very Good
    # 1.75          88-90           Very Good
    # 2.0           85-87           Good
    # 2.25          82-84           Good
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
grade= float(input("Enter your grade percentage: "))

#Step 2: test if 1.0 
if grade >=97 and grade <=100:
    print("Grade mark: 1.00\nDesription: Excellent")
#Step 3: test if 1.25
#Step 4: test if 1.5
#Step 3: test if 1.75
#Step 4: test if 2.0
#Step 3: test if 2.25
#Step 4: test if 2.75
#Step 3: test if 3.0
#Step 4: test if 5.0
#Step 6: test if incomplete, withdrawn, dropped 
