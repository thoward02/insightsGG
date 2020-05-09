"""
    File: insightsGG/Objects/OverwatchAnalytics/Player.py
    Author: Aud#9488
    Desc: This file contains the class for creating player objects
"""

#Import json for dumps
import json

#For the hero list 
class HeroList():
    def __init__(self, StartTime, Hero):
        self.StartTime = StartTime
        self.Hero  = Hero


    #For pretty printing
    def __str__(self):
        return json.dumps(self.toJSON(), indent=4)

    #For pretty json
    def toJSON(self):
        Object = {
            "StartTime" : self.StartTime,
            "Hero" : self.Hero
        }

        return Object

#The actual player
class Player():
    def __init__(self, Id, Name, JsonHeroList):
        #Setup vars
        self.Id = Id
        self.Name = Name
        self.HeroList = []

        #Setup hero list
        for Heroes in JsonHeroList:
            self.HeroList.append(
                HeroList(Heroes["start_time"], Heroes["name"])
            )


    #For pretty printing
    def __str__(self):
        return(
            json.dumps(self.toJSON(), indent=4)
        )

    #For pretty json
    def toJSON(self):
        #Add hero list
        HeroList = []
        for Heroes in self.HeroList:
            HeroList.append(
                Heroes.toJSON()
            )

        #Create object
        Object = {
            "Id" : self.Id,
            "Name" : self.Name,
            "HeroList" : HeroList     
        }

        return Object

    