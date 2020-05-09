"""
    File: insightsGG/Objects/OverwatchAnalytics/FirstEvent.py
    Author: Aud#9488
    Desc: This file contains the class for creating FirstEvent objects
"""

#Import json for dumps
import json

#Ult object
class FirstEvent():
    def __init__(self, InsightsObject):
        if(InsightsObject != ""):
            self.Hero        = InsightsObject["hero"]
            self.PlayerIndex = InsightsObject["player"]
            self.Team        = InsightsObject["team"]

        if(InsightsObject == ""):
            self.Hero        = None
            self.PlayerIndex = None
            self.Team        = None

    def __str__(self):
        return(
            json.dumps(self.toJSON(), indent=4)
        )

    def toJSON(self):
        Object = {
            "Hero" : self.Hero,
            "PlayerIndex" : self.PlayerIndex,
            "Team" : self.Team
        }

        return Object



    