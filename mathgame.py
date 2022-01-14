#############################################
#   Imports
#############################################

#   Import needed for random number generator
import random 

#   Import for clearing out command line screen 
import os

#   Import for countdown timer
import time

#############################################
#   Variables
#############################################

#   Used to define what multiplication set is used. (Fixed Number)
number1 = 1  

#   Used to define what number to multiply number1 against (Randomly Generated)
number2 = 1

#   Answer
answer = 0

#   User's answer
usersAnswer = 1

#   Countdown timer for start of the game
t = 10

#   Number correct in a row to win.
correctNeeded = 20

#   Number correct
correct = 0

#############################################
#   Functions
#############################################

#   Clears out the command prompt.
def clearScreen():                                                                  
    os.system("cls")

#   Title of Game
def title():
    print("-" * 30) 
    print("Multiplicaton Fun Time")
    print("-" * 30, "\n")

#   Countdown timer
def countdown(t):
    print("-" * 30) 
    print("Game Will Start In:")
    print("-" * 30)
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    clearScreen()

#  Defines number1 (multiplication set) from player an sets the "type" to integer
def multiplicationSet():
    global number1
    number1 = int(input("Which multiplication set are you currently studying?\n"))
    clearScreen()

#  Defines number2 as a randomly generated number between 0-12 to multiply against number1
def randomNumber():
    global number2
    number2 = random.randint(0,12)
    return number2

#  New math problem
def newProblem():
    global number1
    global number2
    global answer
    randomNumber()
    answer = number1 * number2

#   Total correct display
def correctDisplay():
    print("-" * 30) 
    print("Correct Needed to Win: ", correctNeeded)
    print("Correct: ", correct)
    print("-" * 30, "\n")

#   Total correct display
def wrongAnswer():
    global usersAnswer
    clearScreen()
    correctDisplay()
    print("")
    print("YOUR ANSWER WAS INCORRECT")
    print (number1, " x ", number2, " = ", answer)
    time.sleep(3)

#   Losing Message
def practice():
    print("-" * 30) 
    print("You're missing a lot.....\nslow down and start again.")
    print("-" * 30, "\n")

#   Win Message
def win():
    print("-" * 30) 
    print("You Win")
    print("-" * 30, "\n")

#  Presents multiplication problem to user and get answer input
def problem():
    global usersAnswer
    global answer
    global correct
    global correctNeeded
    while (correct != -5 and correct != correctNeeded):
        correctDisplay()
        usersAnswer = int(input(str(number1) + " x " + str(number2) + " = " +"\n"))
        if answer == usersAnswer:
            correct += 1
            clearScreen()
            newProblem()            
        elif answer != usersAnswer:
            wrongAnswer()
            correct -= 1
            clearScreen()
            newProblem()
    if correct == -5:
        practice()
    if correct == correctNeeded:
        win()

#   RUN PROGRAM
def run():
    clearScreen()
    title()                                          
    multiplicationSet()
    countdown(t)
    newProblem()
    problem()

#############################################
#   Main
#############################################
run()




