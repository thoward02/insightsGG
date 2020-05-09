"""
    File: insightsGG/Objects/OverwatchAnalytics/Score.py
    Author: Aud#9488
    Desc: This file contains the class for creating score objects
"""

#Import json for dumps
import json


class Score():
    def __init__(self, StartTime, Value):
        self.StartTime = StartTime
        self.Value = Value


    #For pretty printing
    def __str__(self):
        return(
            json.dumps(self.toJSON(), indent=4)
        )

    #For pretty json
    def toJSON(self):
        #Create object
        Object = {
            "StartTime" : self.StartTime,
            "Value"     : self.Value    
        }

        return Object