"""
    File: insightsGG/Objects/OverwatchAnalytics/Ult.py
    Author: Aud#9488
    Desc: This file contains the class for creating ult objects
"""

#Import json for dumps
import json

#Ult object
class Ult():
    def __init__(self, InsightsObject):
        self.Hero = InsightsObject["hero"]
        self.PlayerIndex = InsightsObject["index"]
        try:
            self.Status = InsightsObject["status"]
        except:
            self.Status = None

        if(self.Status == "ready"):
            self.Status = 100



    def __str__(self):
        return(
            json.dumps(self.toJSON(), indent=4)
        )

    def toJSON(self):
        Object = {
            "Hero" : self.Hero,
            "PlayerIndex" : self.PlayerIndex,
            "Status" : self.Status
        }

        return Object



    