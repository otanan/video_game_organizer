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

class EditGameWindow:
    def __init__(self, game):
        self.game = game
        self.window = Toplevel()
        #Counter for how many info nodes have been created
        self.infoNodeCounter = 0
        #Loads the GUI elements of the window
        #since name is not stored in the game.getInfo()
        #we manually do the name information before looping
        self.window.title("Edit: " + self.game.getName())
        self.createInfoNode("Name", self.game.getName())
        gameInfo = self.game.getInfo()
        for info in gameInfo:
            self.createInfoNode(info, gameInfo[info])

    def createInfoNode(self, labelText: str, entryText: str):
        Label(self.window, text=labelText).grid(row=self.infoNodeCounter)
        #Creates the text variable connected to the current text
        #of the entry UI element
        text = StringVar()
        entry = Entry(self.window, textvariable=text)
        text.set(entryText)
        entry.grid(row=self.infoNodeCounter, column=1)
        self.infoNodeCounter += 1


class GameViewer:
    #Dictionary connecting item node information
    #to the game itself
    nodeIDsToGame = {}

    def __init__(self, gamesList):
        #gamesList is a dictionary relating all of the names of games
        #to their Game object
        self.gamesList = gamesList
        self.createWindow()

    def createWindow(self):
        root = Tk()
        root.title("Video Game Organizer v0.00")
        treeview = ttk.Treeview(root)
        treeview.pack()

        #Runs through each game in the games list to create
        #an entry in the GUI then saves the ID to
        #each entry in the nodeIDsToGame
        #mapping the item ID to the game information object
        for gameName in self.gamesList:
            self.nodeIDsToGame[self.createGameNode(treeview, self.gamesList[gameName])] \
                = self.gamesList[gameName]

        #Start listening for events
        treeview.bind("<Double-1>", lambda e : self.openEditWindow(treeview))
        root.mainloop()

    def createGameNode(self, treeview, game):
        nodeID = treeview.insert('', '0', text=game.getName())
        for key in game.getInfo():
            treeview.insert(nodeID, '0', text= (key + ': ' + str(game.getInfo()[key]) ) )
        return nodeID

    def openEditWindow(self, treeview):
        #Opens an edit game window with the Game information passed in
        EditGameWindow(self.nodeIDsToGame[treeview.focus()])


def main():
    GameViewer(game_controller.readGamesFile())

if __name__ == "__main__":
    main()