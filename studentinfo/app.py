'''
	Student App Launcher
'''
from os import system
from studentapi import *

idno:str=""
lastname:str=""
firstname:str=""
course:str=""
level:str=""

student:dict = {}

def header(message:str)->None:
    system('cls')
    print('-'*20)
    print(message.upper().center(20))
    print('-'*20)

def inputstudent()->None:
    global idno,lastname,firstname,course,level
    idno = input("IDNO       :")
    lastname = input("LASTNAME   :")
    firstname = input("FIRSTNAME  :")
    course = input("COURSE     :")
    level = input("LEVEL      :")

def inputstudent_noidno()->None:
    global lastname,firstname,course,level
    lastname = input("LASTNAME   :")
    firstname = input("FIRSTNAME  :")
    course = input("COURSE     :")
    level = input("LEVEL      :")

def add()->None: 
    header('add student')
    inputstudent()
    if idno !="" and lastname !="" and firstname !="" and course !="" and level !="": 
        addstudent(idno=idno,lastname=lastname,firstname=firstname,course=course,level=level)
        print(f"\nNew Student Added...")
    else:
        print(f"\nFill All fields")
    
def find()->None:
    global idno,student
    header('find student')
    idno = input("Student IDNO:")
    student = findstudent(idno=idno)
    print('-'*50)
    for key,value in student.items():
        print(f"{key:>10} : {value:<10}")
    print('-'*50)
    
    
def remove()->None: 
    find()
    opt:str = input("Do you really want to DELETE this student(Y/N):")
    if opt.upper()=="Y":
        deletestudent(student)
        print("Student DELETED !!!")
    else:
        print("Student DELETED Cancelled !!!")
    
def update()->None:
    find()
    opt:str = input("Do you really want to UPDATE this student(Y/N):")
    if opt.upper()=="Y":
        inputstudent_noidno()
        if lastname !="" and firstname !="" and course !="" and level !="": 
            updatestudent(idno=idno,lastname=lastname,firstname=firstname,course=course,level=level)
            print(f"\nStudent Updated...")
        else:
            print(f"\nFill All fields")
    else:
        print("Student Update Cancelled !!!")

def terminate()->None: print("Program Ended...")

def showmenu()->None:
    system('cls')
    print('-'*5+" Main Menu "+'-'*5)
    print('1. Add Student ')
    print('2. Find Student ')
    print('3. Delete Student ')
    print('4. Update Student ')
    print('5. Display All Student ')
    print('0. Quit/End ')
    print('-'*21)

def main()->None:
    option:int = -1
    while option!=0:
        showmenu()
        try:
            option = int(input("Select (0..5):"))
            match option:
                case 1: add()
                case 2: find()
                case 3: remove()
                case 4: update()
                case 5: displayall()
                case 0: terminate()
                case _: print("Accept only 0 to 5")
                
        except Exception as e:
            print(f"Invalid Input: {e}")
        print()
        input("Press any key to continue...")
 
if __name__=="__main__":
	main()