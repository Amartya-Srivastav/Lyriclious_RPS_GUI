from random import *
from tkinter import *

# Choice Code
# left side is user's side and right side is computer's side


def userChoiceRock():
    userChoice = "rock"
    turn(userChoice)
    userImage.configure(image = rockImage)


def userChoicePaper():
    userChoice = "paper"
    turn(userChoice)
    userImage.configure(image = paperImage)


def userChoiceScissors():
    userChoice = "scissors"
    turn(userChoice)
    userImage.configure(image = scissorsImage)

# gameplay code


def turn(userChoice):
    opponent = ['rock', 'paper', 'scissors']
    opponentChoice = opponent[randint(0, 2)]

    if opponentChoice == 'rock':
        opponentImage.configure(image=rockImage)
    elif opponentChoice == 'paper':
        opponentImage.configure(image=paperImage)
    else:
        opponentImage.configure(image=scissorsImage)

    if opponentChoice == userChoice:
        turnResult.configure(text = "It's a draw.", fg = "gray")
        compare.configure(text = "=")
    elif (opponentChoice == 'rock' and userChoice == 'scissors') or (opponentChoice == 'paper' and userChoice == 'rock') or (opponentChoice == 'scissors' and userChoice == 'paper'):
        turnResult.configure(text = "You are defeated!", fg = "red")
        compare.configure(text="<")
    else:
        turnResult.configure(text = "You win!", fg = "green")
        compare.configure(text = ">")

# main code


mainWindow = Tk()
mainWindow.title("Rock-Paper-Scissors by Nrehtron")
rockButton = Button(mainWindow, width = 20, text = "ROCK!", justify = CENTER, command = userChoiceRock, activebackground = 'black', activeforeground = 'white')
paperButton = Button(mainWindow, width = 20, text = "PAPER!", justify = CENTER, command = userChoicePaper, activebackground = 'black', activeforeground = 'white')
scissorsButton = Button(mainWindow, width = 20, text = "SCISSORS!", justify = CENTER, command = userChoiceScissors, activebackground = 'black', activeforeground = 'white')

# Gifs


rockImage = PhotoImage(file = "rock.gif")
paperImage = PhotoImage(file = "paper.gif")
scissorsImage = PhotoImage(file = "scissor.gif")
userImage = Label(image = rockImage)
userImage.image = rockImage
compare = Label(mainWindow, justify = CENTER, font = ("Helvetica", 30) )
opponentImage = Label(image = paperImage)
opponentImage.image = paperImage
turnResult = Label(mainWindow, width = 20, justify = CENTER, font = ("Helvetica", 20) )

# GUI code


rockButton.grid(row = 2, column = 1)
paperButton.grid(row = 2, column = 2)
scissorsButton.grid(row = 2, column = 3)
userImage.grid(row = 3, column = 1)
compare.grid(row = 3, column = 2)
opponentImage.grid(row = 3, column = 3)
turnResult.grid(row = 4, column = 2)

# mainloop


mainWindow.mainloop()