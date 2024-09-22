'''
	Student class
'''
from os import system
from Person import *

class Student(Person):
    def __init__(self,idno:str,lastname:str,firstname:str,mi:str,course:str,level:str):
        super().__init__(lastname,firstname,mi)
        self.idno = idno
        self.course = course
        self.level = level
        
    def __eq__(self,Student): #check if the parameter is the same student object
        return Student.idno==self.idno
        
    def __str__(self):
        return self.idno+" "+super().__str__()+" "+self.course+" "+self.level

def main()->None:
    system('cls')
    student = Student('1000','durano','dennis','s','bscpe','5')
    student1 = Student('2000','durano','dennis','s','bscpe','5')
    
    print(student)
    print(student.__eq__(student1))
    
if __name__=="__main__":
    main()
    