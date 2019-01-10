"""
====================================
Filename:       game_controller.py 
Author:         Jonathan Delgado 
Description:    Module that handles logic of reading and writing to JSON file
====================================
"""
import json

import game

filePath = 'res/games.json'

def readGamesFile():
    with open(filePath) as gameFile:
        #Reads the JSON file for appending, and returns the dictionary
        gamesListAsJSON = json.load(gameFile)

    #Converts the JSON list to Game objects
    gamesList = list()
    for gameName in gamesListAsJSON:
        #Gets the game info dictionary and converts it back to the object
        gamesList.append(game.JSON_to_Game(gameName, gamesListAsJSON[gameName]))

    return gamesList

def appendGameToList(game: game.Game, gamesList: dict):
        gamesList[game.getName()] = game.getInfo()

def saveGamesFile(gamesList):
    #Converts the list of Game objects back into a large dictionary
    #for storing as JSON
    gamesListAsJSON = {}
    for game in gamesList:
        gamesListAsJSON[game.getName()] = game.getInfo()

    #Writes the updated JSON file out
    with open(filePath, 'w') as gameFile:
        json.dump(gamesListAsJSON, gameFile, indent=4)

if __name__ == "__main__":
    gamesList = readGamesFile()

    #Temp, creates a single JSON entry with Shadow of War
    # gamesList = (
    #     game.Game("Shadow of War"),
    #     game.Game("Darksiders II")
    # )


    saveGamesFile(gamesList)