print("WELCOME TO PYTHON QUIZ")
playing=input("DO YOU WANT TO PLAY?")
if playing.lower()!="yes":
    quit()
print("OKAY!! LETS PLAY!!!")
score=0
answer=input("who developed python?")
if answer.lower()=="guida van rossum":
    print("CORRECT ANSWER!!")
    score=+1
else:
    print("INCORRECT ANSWER!!")
answer=input("what is the extension of python files?")
if answer.lower()==".py":
    print("CORRECT ANSWER!!")
    score=+1
else:
    print("INCORRECT ANSWER!!")
answer=input("What are like container that are used to store data?")
if answer.lower()=="variables":
    print("CORRECT ANSWER!!")
    score=+1
else:
    print("INCORRECT ANSWER!!")
answer=input("which is interpreted language?")
if answer.lower=="python":
    print("CORRECT ANSWER!!")
    score=+1
else:
    print("INCORRECT ANSWER!!")
answer=input("Which type of programming does python support?")
if answer.lower=="oops and sp":#structured programming
    print("CORRECT ANSWER!!")
    score=+1
else:
    print("INCORRECT ANSWER!!")
answer=input("What is the maximum length of a identifier?")
if answer.lower=="79":
    print("CORRECT ANSWER")
    score=+1
else:
    print("INCORRECT ANSWER!!")
answer=input("Is python case sensitive when dealing with identifiers?")
if answer.lower=="yes":
    print("CORRECT ANSWER!!")
    score=+1
else:
    print("INCORRECT ANSWER")
answer=input("Is Python code compiled or interpreted?")
if answer.lower=="both":
    print("CORRECT ANSWER!!")
    score=+1
else:
    print("INCORRECT ANSWER!!")
answer=input("Which keyword is used for function in Python language?")
if answer.lower=="def":
    print("CORRECT ANSWER")
    score=+1
else:
    print("INCORRECT ANSWER")
answer=input(" Which  character is used to give single-line comments in Python?")
if answer.lower=="#":
    print("CORRECT ANSWER!!")
    score=+1
else:
    print("INCORRECT ANSWER!!")
print("YOU GOT "+str(score)+" QUESTION ANSWER")
print("YOU HAVE GOT"+str((score/10)*100)+"%")





