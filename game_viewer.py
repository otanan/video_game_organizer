"""
====================================
Filename:       game_viewer 
Author:         Jonathan Delgado 
Description:    Module controlling showing the JSON information to screen
                and creating a GUI for it
====================================
"""

from tkinter import *

import game_controller

def createWindow():
    root = Tk()
    gamesList = game_controller.readGamesFile()
    #Runs through each game in the games list to create
    #an entry in the GUI
    for game in gamesList:
        createGameNode(root, game)

    root.mainloop()

def createGameNode(root, game):
    gameLabel = Label(root, text=game.getName()).grid()

def main():
    createWindow()

if __name__ == "__main__":
    main()