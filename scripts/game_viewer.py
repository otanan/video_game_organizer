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

import game, game_controller

class EditGameWindow:
    #List containing the UI entry elements for each node
    #to save information upon closing
    infoEntries = {}

    def __init__(self, gameViewer, nodeID=None, game=game.Game()):
        self.gameViewer = gameViewer
        self.nodeID = nodeID
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

        #Add save button
        saveButton = Button(self.window, text="Save & Close", command=self.saveGameInfo).grid(row=self.infoNodeCounter + 1)

    def createInfoNode(self, labelText: str, entryText: str):
        Label(self.window, text=labelText).grid(row=self.infoNodeCounter)
        #Creates the text variable connected to the current text
        #of the entry UI element
        text = StringVar()
        entry = Entry(self.window, textvariable=text)
        text.set(entryText)
        entry.grid(row=self.infoNodeCounter, column=1)
        self.infoEntries[labelText] = entry
        self.infoNodeCounter += 1

    def saveGameInfo(self):
        updatedGame = game.Game(name=self.infoEntries['Name'].get(), platform=self.infoEntries['platform'].get(), multiplayer=self.infoEntries['multiplayer'].get())
        self.gameViewer.updateGameInfo(self.nodeID, updatedGame)
        self.window.destroy()


class Toolbar:
    def __init__(self, window):
        self.frame = Frame(window).pack(side="bottom") 

    def addButton(self, text, command):
        Button(self.frame, text=text, command=command).pack()


class GameViewer:
    #Dictionary connecting item node information
    #to the game itself
    nodeIDsToGame = {}

    def __init__(self, gamesList):
        #gamesList is a dictionary relating all of the names of games
        #to their Game object
        self.gamesList = gamesList
        self.createWindow()


    def createGameNode(self, game):
        nodeID = self.treeview.insert('', '0', text=game.getName())
        for key in game.getInfo():
            self.treeview.insert(nodeID, '0', text= (key + ': ' + str(game.getInfo()[key]) ) )
        return nodeID

    def createWindow(self):
        root = Tk()
        root.title("Video Game Organizer v0.00")
        self.treeview = ttk.Treeview(root)
        self.treeview.pack()

        #Runs through each game in the games list to create
        #an entry in the GUI then saves the ID to
        #each entry in the nodeIDsToGame
        #mapping the item ID to the game information object
        for gameName in self.gamesList:
            self.nodeIDsToGame[self.createGameNode(self.gamesList[gameName])] = self.gamesList[gameName]

        #create add button
        toolbar = Toolbar(root)
        #Opens an empty edit game window
        toolbar.addButton("+", lambda: EditGameWindow(self))

        #Start listening for events
        self.treeview.bind("<Double-1>", lambda e: EditGameWindow(self, self.treeview.focus(), self.nodeIDsToGame[self.treeview.focus()]))
        #Set up for saving on close
        root.protocol("WM_DELETE_WINDOW", self.close)
        root.mainloop()

    def updateGameInfo(self, nodeID, game):
        if nodeID is not None:
            self.treeview.delete(nodeID)
        self.nodeIDsToGame[self.createGameNode(game)] = game
        self.gamesList[game.getName()] = game

    def close(self):
        game_controller.saveGamesFile(self.gamesList)


def main():
    GameViewer(game_controller.readGamesFile())

if __name__ == "__main__":
    main()