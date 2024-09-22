'''
	Python OOP
'''
class Person(object):
    def __init__(self,lastname,firstname,mi): #class constructor
        self.lastname = lastname
        self.firstname = firstname
        self.mi = mi
    
    def __str__(self):
        return self.lastname+" "+self.firstname+" "+self.mi

def main()->None:
    person = Person('durano','dennis','s')
    print(person)

if __name__=="__main__":
    main()