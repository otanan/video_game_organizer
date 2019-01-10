"""
====================================
Filename:       game.py 
Author:         Jonathan Delgado 
Description:    Module defining game object for accessing game information
====================================
"""

class Game:
    def __init__(self, name, platform="not owned", multiplayer=False):
        self.name           = name
        self.platform       = platform
        self.multiplayer    = multiplayer
 
    def getName(self):
        return self.name

    #Returns a dictionary containing all of the game's information
    def getInfo(self):
        return {
            "platform": self.platform,
            "multiplayer": self.multiplayer
        }

def JSON_to_Game(gameName: str, gameInfo: dict):
    """
        Helper constructor to convert dictionaries to Game objects
    
        Args:
            gameInfo (dict): the dictionary to be converted
    
        Returns:
            (Game): the converted Game object
    
    """
    return Game(
        gameName,
        gameInfo['platform'],
        gameInfo['multiplayer']
    )