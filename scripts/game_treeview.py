"""
====================================
Filename:       game_treeview.py 
Author:         Jonathan Delgado 
Description:    Treeview controller that handles logic for managing treeview
                where nodes are all game information
====================================
"""

from game import *
from tkinter import ttk

class GameTreeview:
    nodeIDsToGames = {}

    def __init__(self, master):
        self.treeview = ttk.Treeview(master)
        self.treeview.pack()

    def selected(self):
        return self.treeview.focus()

    def getSelectedGame(self):
        return self.getGame(self.selected())

    def delete(self, nodeID):
        self.treeview.delete(nodeID)

    def getGame(self, nodeID):
        #Returns the game object the nodeID is associated with
        #if the nodeID is nothing, simply returns a default game
        return self.nodeIDsToGames[nodeID] if nodeID is not None else Game()

    def createGameNode(self, game: Game):
        nodeID = self.treeview.insert('', '0', text=game.getName())
        for key in game.getInfo():
            self.treeview.insert(
                nodeID,
                '0',
                text= (key.capitalize() + ": " + str(game.getInfo()[key]))
            )
        self.nodeIDsToGames[nodeID] = game