# if, elif, else ladder

a = int(input("Enter Your Age: "))

if(a>=18):
    print("You are Above The Age Of Consent")
    print("You can use this program")
    
elif(a<0):
    print("You are entering an invalid age")
    
elif(a==0):
    print("You are entering an invalid age")
    
else: 
    print("You are below the age of consent", end=", ")
    print("You Cannot Use This Program")
       
print("End Of program") 


#quiz problem 
a = int(input("Enter Your AGE"))

if(a>=18):
    print("yes")
    
else:
    print("no")
