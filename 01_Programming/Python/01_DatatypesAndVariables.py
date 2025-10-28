#variables
a = 1

b = 2

c = 3

#datatypes

a = 1 # a is an integer

b = 2.54 # b is a floating point number

c = "Karan" # c is a string

d = True # d is a boolean

e = None # e is a none type variable

# rules variables

a = 65
karan = 90
_baka = 99

#Operators
karan = "satyawali"
print(karan)

a = 34 
b = 4 
c = a+b
print(c)

#assignment operators
a = 4-2
print(a)

b = 6 #actual value of b constant
b += 5 # increment the value of b by 5 6+5 = 11
print(b)

#comparison operators

d = 5<=5 # result will always be in boolean true or false only in comparison operators
print(d)

e = 7!=8
print(e)

f = 2==3
print(f)

# logical operators

g = True or False
print(g)

# truth table of 'or'
print("True or False is", True or False)
print("True or True is ", True or True)
print("False or True is", False or True)
print("False or False is", False or False)

#truth table of 'and'
print("True and False is", True and False)
print("True and True is ", True and True)
print("False and True is", False and True)
print("False and False is", False and False)

print(not(False))

#type function and typecasting
a = 31.2
b = str(a)
t = type(b)
print(t)

# int(input functions)
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print("Number a is: ", a)
print("Number b is: ", b)
print("Sum is ", a + b)
#practice set

#1
a = 7
b = 4

c = a + b
print(c)

#2
a = 95
b = 8
print("Remainder when a is divided by b is: ", a % b)

#3
a = int(input("Enter the value of a: "))
print(type(a))

#4
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print(a>b)

#5
a = int(input("Please Enter Number 1: "))
b = int(input("Please Enter Number 2: "))
print("The avrage of the two sum is", (a+b)/2)

#6
a = int(input("Enter number 1"))
b = int(input("Enter number 2"))
print("The square of the number is", a*b)
