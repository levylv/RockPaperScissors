#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Lv Wei @ 2016-06-16


#1 = Rock
#2 = Paper
#3 = Scissors

from random import *

# Read initial dataset, Each line is an item
f = open('Init.txt','r')
readFile = []
lines = f.readlines()
for line in lines:
    line = line.rstrip('\n')
    readFile.append(line)
f.close()

readFile[0] = 'The dataset of new player\n' # build new player's dataset
readFile[1] = 'Rounds:1' # reset the round for each player


aDict = {1:'Rock', 2:'Paper', 3:'Scissors'}

def predict(last):
    #where prev is a string, first digit is users last input, second digit is cpu last input
    find = 'move:' + str(last)
    index = readFile.index(find)
    r = readFile[index + 1][2:]
    p = readFile[index + 2][2:]
    s = readFile[index + 3][2:]
    r = int(r)
    p = int(p)
    s = int(s)
    if r > p and r > s:
        return(1)
    elif p > r and p > s:
        return(2)
    elif s > r and s > p:
        return(3)
    elif r == p == s:
        return(randint(1,3))
    elif r == p:
        return(randint(1,2))
    elif p == s:
        return(randint(2,3))
    elif r == s:
        return(int(choice('13')))


def convert(inp):
        #input:user choice,  output:user choice as int
        #change string choice to int value
        if inp.lower() == 'rock' or inp.lower() == 'r':
            choice = 1
        elif inp.lower() == 'paper' or inp.lower() == 'p':
            choice = 2
        elif inp.lower() == 'Scissors' or inp.lower() == 's':
            choice = 3
        return(choice)

def aiMove(tg):
        #input: prediction,  output: chosen move
        #change prediction to AI throw
        if int(tg) == 3:
            guess = 1
        else:
            guess = int(tg) + 1
        return(guess)

#determining who wins
def detwin(c,g):
        #c is choice
        #g is guess
        #figure out who wins
        #winstatus determines if the AI wins

        winstatus = ""
        if c == g:
            winstatus = 'tie'
        elif c == 3 and g == 1:
            winstatus = 'lose'
        elif c == 1 and g ==3:
            winstatus = 'win'
        elif c < g:
            winstatus = 'lose'
        else:
            winstatus = 'win'
        return winstatus



#Changes readList 
def recordResult(l,c):
    find = "move:" + str(l)
    index = readFile.index(find)
    if c == 1:
        a = readFile[index + 1][2:]
        b = int(a) + 1
        readFile[index + 1] = 'r:' + str(b)
    elif c == 2:
        a = readFile[index+2][2:]
        b = int(a) + 1
        readFile[index + 2] = 'p:' + str(b)
    elif c == 3:
        a = readFile[index + 3][2:]
        b = int(a) + 1
        readFile[index + 3] = 's:' + str(b)


def play():
    last = 0
    yourScore = 0
    computerScore = 0
    gameString = readFile[0]

    while True:
        #reset values

        tempguess = 0
        choice = 0
        guess = 0
        isChoiceInputInvalid = True
        while(isChoiceInputInvalid):
            strchoice = raw_input("Choose: Rock, Paper, Scissors, Quit :")
            if strchoice.lower() == 'quit':
                return None
            elif strchoice.lower() == 'rock' or strchoice.lower() =='r':
                strchoice = 'r'
            elif strchoice.lower() == 'paper' or strchoice.lower() == 'p':
                strchoice = 'p'
            elif strchoice.lower() == 'scissors' or strchoice.lower() == 's':
                strchoice = 's'
            if ((strchoice != 'r') and (strchoice != 'p') and (strchoice != 's')):
                print("That is not a valid input, try again")
                isChoiceInputInvalid = True
            else:
                isChoiceInputInvalid = False

        #Choose Difficulty and Predict user choice
        pre = predict(last)


        move = aiMove(pre)  #Convert Prediction to aI throw
        c = convert(strchoice)  #convert user input to user throw
        ws = detwin(c,move)    #Determine who wins
        recordResult(last, c)
        last = str(c) + str(move)   #Used as argument for next round

        print("Round is:" + readFile[1][7:])
        print("Your choice:" + str(aDict[c]))
        print("Computer Choice:" + str(aDict[move]))
        print('Result:' + str(ws))

        if ws == 'win':
            yourScore = yourScore + 1
        elif ws == 'lose':
            computerScore = computerScore + 1

        print("Your Score:" + str(yourScore))
        print("Computer Score:" + str(computerScore))
        print("")

        #Gets and Sets Rounds Played
        a = readFile[1][7:]
        b = int(a) + 1
        readFile[1] = 'Rounds:' + str(b)

        #write results to new Player.txt
        f1 = open('Player.txt','w')
        for x in readFile:
            f1.write(x)
            f1.write('\n')
        f1.close()

# start
play()
