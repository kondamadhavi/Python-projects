import random
top_of_range=input("type a number:")#10
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("Please type a number larger than 0 next time")
        quit()
else:
    print("Please type a number next time.")
    quit()
random_number=random.randint(0,top_of_range)#5
guesses=0
while True:
    guesses+=1
    user_guess=input("make a guess:")#3
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please enter the number next time")
        continue
    if user_guess==random_number:
        print("you got it !!")
        break
    elif user_guess>random_number:
        print("You were above the number")
    else:
        print("You are below the number")
print("You got it in",guesses,"guesses")
