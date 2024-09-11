'''
	student api(application programming interface)
'''
from os import system
from data import slist

index:int = 9999999

def addstudent(**kwargs)->None:  
    slist.append(kwargs)
def findstudent(**kwargs)->None:
    global index
    keys:list = list(kwargs.keys())
    values:list = list(kwargs.values())
    for student in slist:
        if student[keys[0]] == values[0]:
            index = slist.index(student)
            return student
    return None
    
def deletestudent(student)->None:
    slist.remove(student)

def updatestudent(**kwargs)->None:
    slist[index] = kwargs
    
def displayall()->None:
    system('cls')
    keys:list = list(slist[0].keys())
    print('student list'.upper())
    print('-'*100)
    [print(f"{key.upper():>15}",end=" ") for key in keys]#list comprehension
    print()
    print('-'*100)
    for student in slist:
        print(f"{student['idno']:>15}",end=" ")
        print(f"{student['lastname']:>15}",end=" ")
        print(f"{student['firstname']:>15}",end=" ")
        print(f"{student['course']:>15}",end=" ")
        print(f"{student['level']:>15}",end=" ")
        print() #goto next line
    print('-'*100)
    print('nothing follows'.upper().center(100))
 