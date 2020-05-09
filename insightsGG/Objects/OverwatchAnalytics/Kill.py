"""
    File: insightsGG/Objects/OverwatchAnalytics/Kill.py
    Author: Aud#9488
    Desc: This file contains the class for creating Kill / Death objects
"""

#Import json for dumps
import json


class Kill():
    def __init__(self, InsightsObject):
        self.Team = InsightsObject["color"]
        self.Hero = InsightsObject["hero"]


    #For pretty printing
    def __str__(self):
        return(
            json.dumps(self.toJSON(), indent=4)
        )

    #For pretty json
    def toJSON(self):
        #Create object
        Object = {
            "Team" : self.Team,
            "Hero" : self.Hero
        }

        return Object