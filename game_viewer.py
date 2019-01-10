"""
====================================
Filename:       game_viewer.py
Author:         Jonathan Delgado 
Description:    Module controlling showing the JSON information to screen
                and creating a GUI for it
====================================
"""
from tkinter import *
from tkinter import ttk

import game_controller

def createWindow():
    root = Tk()
    treeview = ttk.Treeview(root)
    treeview.pack()

    gamesList = game_controller.readGamesFile()
    #Runs through each game in the games list to create
    #an entry in the GUI
    for game in gamesList:
        createGameNode(treeview, game)

    #Start listening for events
    treeview.bind("<<TreeviewSelect>>", callback)
    root.mainloop()

def createGameNode(treeview, game):
    nodeID = treeview.insert('', '0', text=game.getName())
    for key in game.getInfo():
        treeview.insert(nodeID, '0', text= (key + ': ' + str(game.getInfo()[key]) ) )

def callback(event):
    print("Hello world")


def main():
    createWindow()

if __name__ == "__main__":
    main()