'''
Rules of the game:
-> This game is basically another version of rock,paper and scissor.
-> First there are choices of three moves snake, water and gun.
-> we used the dictionary method to set the game rules.
-> if the user type q or quit it will quit the game.
-> if the user type any other move which is not in the choices list then it will print "invalid move".
-> and then after user typed his/her choice move then using the import function we generate a random choice from the computer from these three choices.
-> and finally the result time! if the user and the computer choice is same them the resukt will be tie.
-> if the user wins it prints "you win!" and if the loser loses then it prints "You lose"
-> That`s it i am still learning python and this is my first mini project. 
-> This code can be done by many other methods.
-> my linkedin:- https://www.linkedin.com/in/karan-satyawali-366a2337a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app

'''

import random

choices = ["snake", "water", "gun"]
rules = {
  ("snake", "water"): "snake",
  ("water", "gun"): "water",
  ("gun", "snake"): "gun"
}

while True:
    user = input("Enter snake/wate/gun or q to quit").lower()
    if user in ("q", "quit"):
        break
    if user not in choices:
        print("Invalid move!\n")
        continue
    comp = random.choice(choices)
    print(f"You: {user} | Computer: {comp}")
    
    if user == comp:
        print("Result: Tie!\n")
        
    elif rules.get((user, comp)) == user:
        print("Result: You win!\n")
        
    else:
        print("Result: Computer wins!\n")
