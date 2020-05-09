"""
    File: insightsGG/Objects/OverwatchAnalytics/Event.py
    Author: Aud#9488
    Desc: This file contains the class for creating event objects
"""

#Import json for dumps
import json

#For Kill Obejcts
import insightsGG.Objects.OverwatchAnalytics as OWAnalytics


class Event():
    def __init__(self, InsightsObject):
        self.Type    = InsightsObject["type"]
        self.Time    = InsightsObject["time"]

        if(InsightsObject["type"] == "kill"):
            self.Ability = InsightsObject["ability"]
            self.Assists = InsightsObject["assists"]
            self.Killee = OWAnalytics.Kill(InsightsObject["killee"])
            self.Killer = OWAnalytics.Kill(InsightsObject["killer"])
            

        if(InsightsObject["type"] == "suicide"):
            self.Hero = InsightsObject["hero"]
            self.Team = InsightsObject["team"]


    #For pretty printing
    def __str__(self):
        return(
            json.dumps(self.toJSON(), indent=4)
        )

    #For pretty json
    def toJSON(self):
        #Create object
        Object = {
            "Type" : self.Type,
            "Time" : self.Time
        }
        
        if(self.Type == "kill"):
            Object["Ablity"] = self.Ability
            Object["Assists"] = self.Assists
            Object["Killee"] = self.Killee 
            Object["Killer"] = self.Killer 
            

        if(self.Type == "suicide"):
            Object["Hero"] = self.Hero
            Object["Team"] = self.Team 

        return Object