"""
====================================
Filename:       game_viewer.py
Author:         Jonathan Delgado 
Description:    Module controlling showing the JSON information to screen
                and creating a GUI for it
====================================
"""
from tkinter import *

import game_controller
from game import *
from game_treeview import *

class EditGameWindow:
    infoEntries = {}

    def __init__(self, gameViewer, nodeID=None):
        self.gameViewer = gameViewer
        self.nodeID = nodeID
        self.window = Toplevel()
        gameToEdit = gameViewer.gameTree.getGame(self.nodeID)
        self.window.title("Edit: " + gameToEdit.getName())
        self.frame = Frame(self.window)
        self.frame.pack()

        self.infoNodeCounter = 0
        self.createInfoNode("Name", gameToEdit.getName())
        gameInfo = gameToEdit.getInfo()
        for info in gameInfo:
            self.createInfoNode(info.capitalize(), gameInfo[info])

        toolbar = Frame(self.window)
        toolbar.pack(side="bottom", fill="x")
        #Add Save & Close button
        Button(toolbar, text="Save & Close", command=self.saveGameInfo).pack()

    def getInput(self, key):
        return self.infoEntries[key].get()

    def saveGameInfo(self):
        updatedGame = Game(
            self.getInput("name"),
            platform=self.getInput("platform"),
            multiplayer=self.getInput("multiplayer")
        )
        self.gameViewer.updateGameInfo(self.nodeID, updatedGame)
        #Closes the window for Save & Close
        self.window.destroy()

    def createInfoNode(self, labelText, entryText):
        Label(self.frame, text=labelText).grid(row=self.infoNodeCounter)
        #Creates the text variable connceted to the current text
        #of the entry UI element
        text = StringVar()
        entry = Entry(self.frame, textvariable=text)
        text.set(entryText)
        entry.grid(row=self.infoNodeCounter, column=1)
        self.infoEntries[labelText.lower()] = entry
        self.infoNodeCounter += 1



class GameViewer:
    def __init__(self, gamesList):
        #gamesList is a dictionary relating all of the names of games to their
        #game object
        self.gamesList = gamesList
        self.createWindow()

    def deleteGame(self, game: Game):
        #deletes the node
        self.gameTree.delete(self.gameTree.selected())
        #deletes the game from the list itself to prevent from being saved
        del self.gamesList[game.getName()]


    def close(self):
        game_controller.saveGamesFile(self.gamesList)

    def updateGameInfo(self, nodeID, game: Game):
        if nodeID is not None:
            self.gameTree.delete(nodeID)
        self.gameTree.createGameNode(game)
        self.gamesList[game.getName()] = game

    def createWindow(self):
        root = Tk()
        root.title("Video Game Organizer v0.01")
        frame = Frame(root)
        frame.pack()
        self.gameTree = GameTreeview(frame)
        #Loads the game nodes
        for gameName in self.gamesList:
            self.gameTree.createGameNode(self.gamesList[gameName])

        #Creates toolbar with add, delete, etc. buttons
        toolbar = Frame(root)
        toolbar.pack(side="bottom", fill="x")
        Button(toolbar, text="+", command=lambda: EditGameWindow(self)).pack(fill="x")        
        Button(toolbar, text="-", command=lambda: self.deleteGame(self.gameTree.getSelectedGame())).pack(fill="x")
        #Start listening for double click events
        self.gameTree.treeview.bind("<Double-1>", lambda e: EditGameWindow(self, nodeID=self.gameTree.selected()))
        #Set up for saving on closee
        root.protocol("WM_DELETE_WINDOW", self.close)
        root.mainloop()     


def main():
    GameViewer(game_controller.readGamesFile())

if __name__ == "__main__":
    main()