#!/usr/bin/env python
from Tkinter import *
import random
import Tkinter
from Tkinter import *
import sys
import os
import time
'''
class App(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        master.minimisze(width=500,height=500)
        self.grid()
        self.widget()
        self.word='''
def jumble(string):
    return ' '.join([''.join(random.sample(word, len(word))) for word in string.split()])

#Intialising Game

#Getting data from txt file
array=[]
with open('tvshows.txt','r') as input_file:
    for data in input_file:
        array.append(data.rstrip('\n'))

def game_array():
    #Selecting Random 10 TV shows
    game_list = random.sample(array,10)
    #print(game_list)
    return game_list
def jumble_array():
    #Jumbling data
    jumble_list = []
    for word in game_list:
        jumble_list.append(jumble(word))
    #print(jumble_list)
    return jumble_list

#Initialise Player
def player():
    print("Enter player name: ")
    player1 = raw_input()
def again():
    global score
    global pointer
    global txt_guess
    #print(pointer)
    label_jumbled.config(text=jumble_list[pointer])
    txt_guess = Tkinter.Entry(root,width=30)
    txt_guess.grid(row=4, column=0, padx=5, pady=10)
    btn_check = Tkinter.Button(root, text="Check",fg="green",command=game)
    btn_check.grid(row=6, column=0, sticky=W)
    
    #Start game
def game():
    global score
    global pointer
    global txt_guess
    '''#score = 0#initialise score
        #for index in range(1,len(jumble_list)):
        label_jumbled = Tkinter.Label(root, text=jumble_list[index])
        label_jumbled.grid(row=1, column=0, sticky=E, pady=5)
            #print("Guess the jumbled name of TV Show",jumble_list[index])
            #word = raw_input()
            #word = word.upper()'''
    player_guess = txt_guess.get()
    player_guess = player_guess.upper()
    if player_guess == game_list[pointer]:
        score += 1
        string = "Score: %s" %score
        scored.config(text=str(score) + '/10')
        o.config(text=" ")
        Label(root,text="Correct Answer").grid(row=7,column=0,sticky=W)
        print("Correct Answer",string)
        pointer+=1
    else:
        print("Game Over")
        Label(root,text="Correct Answer was: ").grid(row=8,column=0,sticky=W)
        o.config(text=game_list[pointer])
        Label(root,text="Wrong Answer").grid(row=7,column=0,sticky=W)
        print("Correct answer was: ",game_list[pointer])
        '''time.sleep(1)
        os.system("python gdg.py")
        time.sleep(0.2)
        quit()'''
    if score == 10:
        print("CONGRATULATIONS!! YOU WIN")
        Label(root,text="CONGRATULATIONS!! YOU WIN").grid(row=7,column=0,sticky=W)
    elif score<10:
        #pointer += 1
        again()
        #print("BETTER LUCK NEXT TIME")
           # reset()
def main():
    player()
    game()

    #Start Game
game_list = game_array()
jumble_list = jumble_array()
score = 0
pointer = 0
root = Tk()
root.title("GDG Project")
root.geometry("320x200")
    #Widgets
label_title = Tkinter.Label(root, text="                    Welcome to the Guessing Game!               ")
label_title.grid(row=0, column=0, sticky=W)
label_jumble = Tkinter.Label(root, text = " Scrambeled Show -")
label_jumble.grid(row=1, column=0, sticky=W, pady=5)
player_guess = Tkinter.Label(root, text=" Guess the Show ")
player_guess.grid(row=3,column=0,sticky=W)
txt_guess = Tkinter.Entry(root,width =30)
txt_guess.grid(row=4, column=0, padx=5, pady=10)

o=Label(root,text='')
o.grid(row=8,column=0,sticky=E)
label_jumbled = Tkinter.Label(root, text=jumble_list[pointer])
label_jumbled.grid(row=1, column=0, sticky=E, pady=5)    
    
    #Button
btn_check = Tkinter.Button(root, text="Check",fg="green",command=game)
btn_check.grid(row=6, column=0, sticky=W)
score_label = Tkinter.Label(root, text="Your Score: ")
score_label.grid(row=12,column=0,sticky=W)
scored = Tkinter.Label(root, text = str(score) + '/10')
scored.grid(row=12,column=1,sticky=W)
    #print(game_list,jumble_list)
root.mainloop()
#main()
    
'''#Reseting the game
def reset():
    while True:
        game_start()

reset()'''
