import random
#user score
user_wins=0
#computer science
computer_wins=0
options=["rock","paper","scissor"]
while True:
    user_input=input("type:rock or paper or scissor or q for quitting!!!").lower()
    if user_input=="q":
        break
    if user_input not in options:
        continue
    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    print("computer picked",computer_pick)
    if user_input=="rock" and computer_pick=="scissors":
        print("You won!")
        user_wins+=1
    elif user_input=="paper" and computer_pick=="rock":
        print("You won!!")
        user_wins+=1
    elif user_input=="scissors" and computer_pick=="paper":
        print("You won!!")
        user_wins+=1
        
