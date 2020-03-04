"""
    File: insightsGG/Objects/OverwatchAnalytics/Match.py
    Author: Aud#9488
    Desc: This file contains the class for creating insights Match objects, where
          Match is the analyzed match returned from a GetAnalysis call.
"""
#import json for pretty print
import json

#Import named tuples
from collections import namedtuple


#Import our library
import insightsGG.Objects.OverwatchAnalytics as OWAnalytics

class Match():
    def __init__(self, InsightsObject):
        #Identification
        self.Id          = InsightsObject["id"]
        self.AnalysisId  = InsightsObject["analysis"]["id"]
        self.DateCreated = InsightsObject["created"]
        self.Owner       = {
            "Id"   : InsightsObject["id"],
            "Name" : InsightsObject["name"],
        }

        #Video specififcs
        self.StartTime   = InsightsObject["gstartTime"]
        self.EndTime     = InsightsObject["gendTime"]


        #Analysis data - Map Data
        self.Map            = InsightsObject["data"]["map"]
        self.MapConfidence  = InsightsObject["data"]["map_confidence"]
        self.Gamemode       = InsightsObject["data"]["gamemode"]

        #Analysis data - Score Data
        self.FinalLeftScore = InsightsObject["data"]["final_left_score"]
        self.FinalLeftScore = InsightsObject["data"]["final_right_score"]

        #Analysis data - Player data
        self.BluePlayers    = []
        self.RedPlayers     = []

        Player = namedtuple("Player", "Id Name Heroes")
        Hero   = namedtuple("Hero", "Hero StartTime")

        Counter = 0
        for Players in InsightsObject["data"]["players"]:
            #Create hero list
            HeroList = []
            for HeroObjs in Players["heroes"]:
                HeroList.append(Hero(HeroObjs["name"], HeroObjs["start_time"]))

            #Create player
            ThisPlayer = Player(InsightsObject["data"]["player_ids"][Counter], Players["name"], HeroList)

            #Assign player
            if Counter < 6:
                self.BluePlayers.append(ThisPlayer)
            if Counter >= 6:
                self.RedPlayers.append(ThisPlayer)

            Counter += 1



        print(self.BluePlayers[0].Id)
