import random
n =  random.randint(1,100)
number = -1
guesses = 0

print("Welcome To The Perfect Guess Game")

while number!=n:
    number = int(input("Enter The Number"))
    guesses+=1
    
    if number>n:
        print("Lower Number Please")
        
    elif number<n:
        print("Higher Number Please")
        
    else:
        print(f"You Guessed It Right In {guesses} Attempt")
