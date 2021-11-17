#Program 1: PUP Grading System
#Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description

#Step 1: ask for student grade in percentage, convert, and store
# Can round off grades
print ("\nPolytechnic University of the Philippines Grading System")
print("\nPlease enter your grade percentage here. Type 'N' or 'No grade' if you do not attain any grade.")

while True:
    try:
        quest_grade= float(input(">  ")) 
        roundOffGrade = round(quest_grade)

#Step 2: test if 1.0 
        if roundOffGrade >=97 and roundOffGrade <=100:
            print("\nGrade/Mark: 1.00\nDesription: Excellent\n")
#Step 3: test if 1.25
        elif roundOffGrade >=94 and roundOffGrade <=96:
            print("\nGrade/Mark: 1.25\nDesription: Excellent\n")
#Step 4: test if 1.5
        elif roundOffGrade >=91 and roundOffGrade <=93:
            print("\nGrade/Mark: 1.50\nDesription: Very Good\n")
#Step 3: test if 1.75
        elif roundOffGrade >=88 and roundOffGrade <=90:
            print("\nGrade/Mark: 1.75\nDesription: Very Good\n")
#Step 4: test if 2.0
        elif roundOffGrade >=85 and roundOffGrade <=87:
            print("\nGrade/Mark: 2.00\nDesription: Good\n")
#Step 3: test if 2.25
        elif roundOffGrade >=82 and roundOffGrade <=84:
            print("\nGrade/Mark: 2.25\nDesription: Good\n")
#Step 4: test if 2.5
        elif roundOffGrade >=79 and roundOffGrade <=81:
            print("\nGrade/Mark: 2.5\nDesription: Satisfactory\n")
#Step 3: test if 2.75
        elif roundOffGrade >=76 and roundOffGrade <=78:
            print("\nGrade/Mark: 2.75\nDesription: Satisfactory\n")
#Step 4: test if 3.0
        elif roundOffGrade == 75:
            print("\nGrade/Mark: 3.00\nDesription: Passing\n")
#Step 5: test if 5.0
        elif roundOffGrade >=65 and roundOffGrade <=74:
            print("\nGrade/Mark: 5.00\nDesription: Failure\n")
#Step 6: test if incomplete, withdrawn, dropped 
        else:
            print("\nThe grade you entered is invalid. Grade percentage must be in positive numbers and not greater than 100.\n")
        break
    except ValueError:
        #The following questions is also connected to Section 8 "Grading System"

        print("\nPlease answer the following questions to know if your status is Incomplete, Withdrawn or Dropped.")
        majorExam=input("\n1. Have you taken your major exam?\nType Y if Yes and N if No: ")
        withdrawn= input ("\n2. Have you written a letter to withdraw your enrollment?\nType Y if Yes and N if No: ")
        absent= input ("\n3. Have you been absent ten (10) times in the semester?\nType Y if Yes and N if No: ")
    
        if (majorExam== "N" and withdrawn == "N") and (absent=="N"):
            print("\nGrade Mark: Inc.\nDescription: Incomplete.\n")
        elif (majorExam== "Y") and (withdrawn == "N" or absent== "N"):
            print("\nIt looks like there is a problem occurred.\nPlease ask your teacher for clarification.\n")
        elif majorExam== "N" and withdrawn == "Y":
            print("\nGrade Mark: W\nDescription: Withdrawn\n\nA Withdrawn Mark is given when the student voluntarily withdraws in writing from a subject\nat any time but not less than one (1) month before the final examination\n")
        else:    
            print("\nGrade Mark: D\nDescription: Dropped\n\nYour teacher gave you a dropped mark for exceeding the allowable number\nof absences or for not attending class since the start of the term.\n")
        break
