import random

while True:
    gamer_input = input("Input your choice of weapon, rock, paper, or scissors: ")
    if gamer_input=("stop"):
        break
    computer_input = random.randint(1,3) #1 is rock, 2 is paper, 3 is scissors
    if computer_input ==1:
     print("i play rock!")
    elif  computer_input ==2:
     print("i play paper")

    elif  computer_input ==3:
     print("i play scissors")

    if computer_input ==1 and gamer_input== "rock":
        print("draw")

    elif computer_input ==1 and gamer_input== "scissors":
        print("you lose hehehhehehhe!")
    elif computer_input ==1 and gamer_input== "paper":
        print("you win! good job")


    if computer_input ==2 and gamer_input== "rock":
         print("you lose hehehhehehhe!")

    elif computer_input ==2 and gamer_input== "paper":
        print("draw")
    elif computer_input ==2 and gamer_input== "scissors":
         print("you win! good job")
    

    if computer_input ==3 and gamer_input== "rock":
        print("you win! good job")

    elif computer_input ==3 and gamer_input== "paper":
        print("you lose hehehhehehhe!")
    elif computer_input ==3 and gamer_input== "scissors":
        print("draw")

 
