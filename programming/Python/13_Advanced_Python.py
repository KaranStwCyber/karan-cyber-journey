# WALRUS OPERATOR

# Using walrus operator 
if (n := len([1, 2, 3, 4, 5])) > 3: 
    print(f"List is too long ({n} elements, expected <= 3)") 
# Output: List is too long (5 elements, expected <= 3) 

# TYPING FUNCTION


# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 1, 2, 3)

print(type(person))

# Dictionary with string keys and integer values

scores: Dict[str, int] = {"Alice": 30, "Karan": 20}
print(type(scores))

#union type for variables that can hold multiple values

identifier: Union[int, str] = "526657"
identifier = 1234567
print(type(identifier))

# MATCH CASE

def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"
        
print(http_status(200))

# DICTIONARY MERGE
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = dict1 | dict2
print(merged)
 
# EXCEPTION HANDLING
try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as e:
    print(e)


print("Hello, Guys This code is running")

# EXCEPTION HANDILING

a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b==0):
    raise ZeroDivisionError("Hey you cannot divide any number by zero!")

else:
    print(f"The division of a/b is {a/b}")
    
# TRY WITH ELSE

try:
    a = int(input("Enter a number: "))
    print(a)
    
except Exception as e:
    print(e)
    
else:
    print("Else is running fine!")
    
# TRY WITH FINALLY

def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        
    except ValueError:
        print("Please Enter A Valid Number")
        
    finally:
        print("Finally is running fine!")
        
main()

# IF __NAME__== ‘__MAIN__’ IN PYTHON 

def myFunc():
    print("Hello Gamer!")

if __name__ == "__main__":
    print("We are directly running this code")  
    myFunc()
    
    print(__name__) # If the function is in the same code then it will print __main__ otherwise it will print the name of the file where we imported the function.


# GLOBAL KEYWORD

a = 89

def fun():
    global a
    a = 3
    print(a)
    
fun()
print(a)

# ENUMERATE FUNCTION IN PYTHON

l = [1,44,65,64,78,965]

# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index+=1
    
# this can be simplified using enumerate function

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")
    
# LIST COMPREHENSIONS

myList = [1,2,3,4,6,7,9]
# squaredList = []

# for item in myList:
#     squaredList.append(item*item)

squaredList = [i*i for i in myList] # list comprehensions 
    
print(squaredList)
