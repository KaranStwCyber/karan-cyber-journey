# OBJECT ORIENTED PROGRAMMING

#CLASS

class employee:
    language = "Python" # this is a class attribute
    salary = 13000000
    
    
karan = employee()
karan.name = "Satyawali" # this is an instance attribute
print(karan.name, karan.language, karan.salary)

rohan = employee()
rohan.name = "Bankai katenkyokotsu karamatsu shinju"
print(rohan.name, rohan.salary, rohan.language)

# instance vs class attribute 

class employee:
    language = "Python"
    salary = 12000000
    
karan = employee()
karan.language = "JavaScript" # instance attribute takes prefernce over class attribute so here JavaScript will print
print(karan.language, karan.salary)

# SELF

class employee:
    language = "Python"
    salary = 12000000
    
    def getInfo(self):
        print(f"The salary is {self.salary}, and the language is {self.language}")
     
    @staticmethod   # used when we don`t want this function to take any value from object and with this we don`t have to add self to functions to work with it.
    def greet():
        print("Good morning")
        
karan = employee()
karan.language = "JavaScript"
# karan.getInfo()
employee.getInfo(karan)
karan.greet()

#constructor

class Employee:
    language = "python"
    salary = 1234567890
    
    def __init__(self, name, language, salary):
        self.name = name
        self.language = language
        self.salary = salary
        print("Dunder method is working")
        
    @staticmethod     
    def greet():
        print("Good morning")
            
    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")
            
karan = Employee("Karan", "JavaScript", 1300000000)
print(karan.name, karan.language, karan.salary)
karan.getInfo()
