#FUNCTIONS

#function definition
def avg():
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    c = int(input("Enter number 3: "))
    
    average = (a + b + c)/3
    
    print("The average of the numbers is: ", average)
    
avg() # function call

# Quick Quiz:  Write a program to greet a user with “Good day” using functions.

def greet():
    name = input("Enter your name: ")
    print("Good day!", name)
greet()

# functions with arguments 

def GoodDay(name):
    print("Good DAY", name)
    return "Done"

a = GoodDay("Satyawali bhai")
print(a)

# default parameter value 

def greet(name, ending="Thank You!"):
    print("Good Day", name)
    print(ending)
    
greet("Karan Bhai", "Satyawali")
greet("Rohan")

# recursions

def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n * factorial(n-1)
n = int(input("Enter a number: "))
print("The factorial of this number is", factorial(n))
