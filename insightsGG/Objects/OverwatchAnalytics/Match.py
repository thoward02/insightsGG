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
        self.FinalBlueScore = InsightsObject["data"]["final_left_score"]
        self.FinalRedScore = InsightsObject["data"]["final_right_score"]

        #Analysis data - Player data
        self.BluePlayers    = []
        self.RedPlayers     = []

        Counter = 0
        for Players in InsightsObject["data"]["players"]:
            #Create player
            ThisPlayer = OWAnalytics.Player(
                InsightsObject["data"]["player_ids"][Counter],
                Players["name"],
                Players["heroes"]
            )

            #Assign player
            if Counter < 6:
                self.BluePlayers.append(ThisPlayer)
            if Counter >= 6:
                self.RedPlayers.append(ThisPlayer)

            Counter += 1

        #Analysis data - Roster Ids
        self.BlueRosterId = InsightsObject["data"]["roster_ids"][0]
        self.RedRosterId = InsightsObject["data"]["roster_ids"][1]


        #Analysis data - Score Data
        self.BlueScoreEvents = []
        self.RedScoreEvents = []
      
        for ScoreEvents in InsightsObject["data"]["left_score"]:
            self.BlueScoreEvents.append(OWAnalytics.Score(ScoreEvents["start_time"], ScoreEvents["value"]))

        for ScoreEvents in InsightsObject["data"]["right_score"]:
            self.RedScoreEvents.append(OWAnalytics.Score(ScoreEvents["start_time"], ScoreEvents["value"]))


        #Analysis data - TeamFights
        self.TeamFights = []
        for Teamfights in InsightsObject["data"]["teamfights"]:
            self.TeamFights.append(
                OWAnalytics.TeamFight(Teamfights)
            )



    #Pretty print objects
    def __str__(self):
        return json.dumps(self.toJSON(), indent=4)

    #Pretty json
    def toJSON(self):
        #This is gonna be hella large so we're gonna drop it by taking big lists and turning them into counts
        BluePlayerLen = len(self.BluePlayers)
        RedPlayerLen = len(self.RedPlayers)

        #Create objects
        BlueScoreEvents = []
        for Events in self.BlueScoreEvents:
            BlueScoreEvents.append(
                Events.toJSON()
            )

        RedScoreEvents = []
        for Events in self.RedScoreEvents:
            RedScoreEvents.append(
                Events.toJSON()
            )


        Object = {
            "Id"              : self.Id,
            "AnalysisId"      : self.AnalysisId,
            "DateCreated"     : self.DateCreated,
            "Owner"           : self.Owner,
            "StartTime"       : self.StartTime,
            "EndTime"         : self.EndTime,
            "Map"             : self.Map,
            "MapConfidence"   : self.MapConfidence,
            "Gamemode"        : self.Gamemode,
            "FinalLeftScore"  : self.FinalBlueScore,
            "FinalRightScore" : self.FinalRedScore,
            "BluePlayers"     : "List of {} players".format(BluePlayerLen),
            "RedPlayers"      : "List of {} players".format(RedPlayerLen),
            "BlueRosterId"    : self.BlueRosterId,
            "RedRosterId"     : self.RedRosterId,
            "BlueScoreEvents" : BlueScoreEvents,
            "RedScoreEvents"  : RedScoreEvents,
            "TeamFights" : "List of {} Teamfights".format(len(self.TeamFights))
        }

        return Object
