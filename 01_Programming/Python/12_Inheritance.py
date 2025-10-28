class Employee:
    company = "ITC"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")
        
class programmer(Employee):
    company = "ITC InfoTech"
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
    
    
    
    def showLanguage(self):
        print(f"The name of the employee is {self.name} amd he is good at {self.language}")
        
a = Employee("Karan", 1200000)
b = programmer("Rohan", 3000000, "JavaScript")

print(a.company)
b.show()
print(b.company)
b.showLanguage()
        
     
#  multi level inheritance

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def show(self):
        print(f"The name of the employee is {self.name} and salary is {self.salary}")
        
class programmer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
        
    def showLanguages(self):
        print(f"The name of the employe is {self.name} and salary is {self.salary} and language is {self.language}")
        
class Manager(programmer):
    def __init__(self, name, salary, language, age):
        super().__init__(name, salary, language)
        self.age = age
        
    def managerdetails(self):
        print(f"The name of the employee is {self.name}, and salary is {self.salary}, language known is {self.language}, and age is {self.age}")
        

c = Manager("Satyawali", 300000, "Rust", 24)        
a = Employee("Karan", 100000)
b = programmer("Rohan", 30000, "Python")
a.show()
b.showLanguages()
c.managerdetails()


# CLASS METHODS

# CLASS METHOD

class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attributor of class employee is {cls.a}")
        
        
e = Employee()
e.a = 45
e.show()

# PROPERTY DECORATOR

class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute is {cls.a}")
        
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        
      self.fname = value.split(" ")[0]
      self.lname = value.split(" ")[1]
      
e = Employee()
e.a = 45
e.name = "Karan Satyawali"
print(e.fname, e.lname)
e.show()
