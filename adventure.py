name=input("type your name!")
print("Welcome", name,"to this adventure!!")
answer=input("You are on a dirt road,it has come to an end and you can go left or right.Which way would you like to go?").lower()
if answer=="left":
    answer=input("You come to a river,you can walk around it or swim across?type walk to walk around and swim if you want to swim across:")
    if answer=="swim":
        print("You swim across the river and were eaten by an alligator")
    elif answer=="walk":
       print("You walked miles,ran out of water and lost the game.")
    else:
        print("Not a valid option,You lose")
elif answer=="right":
    answer=input("You came across a bridge,it looks wobbly,do you want to cross it or head back(cross/back)?")
    if answer=="back":
        print("You go back and lose")
    elif answer=="cross":
        answer=input("You cross the bridge and met a stranger.Do you want to talk to him(yes/no)")
        if answer=="yes":
            print("You talk to the stranger and they gift you the treasure.You won!!")
        elif answer=="no":
            print("You ignore the stranger and they get offended and you lose!!")
        else:
            print("Invalid option you lose")
    else:
        print("Invalid option you lose")
else:
    print("Invalid option you lose!!")
print("Thank you for trying","name ")