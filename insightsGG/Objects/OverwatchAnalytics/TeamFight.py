"""
    File: insightsGG/Objects/OverwatchAnalytics/TeamFight.py
    Author: Aud#9488
    Desc: This file contains the class for creating TeamFight objects
"""

#Import json for dumps
import json

#For ults
import insightsGG.Objects.OverwatchAnalytics as OWAnalytics


class TeamFight():
    def __init__(self, InsightsObject):
        #Fight timings
        self.StartTime = InsightsObject["start_time"]
        self.EndTime = InsightsObject["end_time"]

        #Fight winner
        self.Winner = InsightsObject["winner"]

        #Heroes
        self.BlueHeroes = InsightsObject["blue_heroes"]
        self.RedHeroes = InsightsObject["red_heroes"]

        #Blue KDA
        self.BlueKills = InsightsObject["blue_team_kills"]
        self.BlueDeaths = InsightsObject["blue_team_deaths"]
        self.BlueUltKills = InsightsObject["blue_team_ult_kills"]

        #Red KDA
        self.RedKills = InsightsObject["red_team_kills"]
        self.RedDeaths = InsightsObject["red_team_deaths"]
        self.RedUltKills = InsightsObject["red_team_ult_kills"]

        #Setup ults
        self.BlueUltsBefore = []
        self.BlueUltsUsed   = []
        self.BlueUltsAfter  = []

        #Blue Ults
        for Ults in InsightsObject["blue_team_ults_before"]:
            self.BlueUltsBefore.append(
                OWAnalytics.Ult(Ults)
            )

        for Ults in InsightsObject["blue_team_ults_used"]:
            self.BlueUltsUsed.append(
                OWAnalytics.Ult(Ults)
            )

        for Ults in InsightsObject["blue_team_ults_after"]:
            self.BlueUltsAfter.append(
                OWAnalytics.Ult(Ults)
            )

        #Red ults
        self.RedUltsBefore = []
        self.RedUltsUsed   = []
        self.RedUltsAfter  = []

        for Ults in InsightsObject["red_team_ults_before"]:
            self.RedUltsBefore.append(
                OWAnalytics.Ult(Ults)
            )

        for Ults in InsightsObject["red_team_ults_used"]:
            self.RedUltsUsed.append(
                OWAnalytics.Ult(Ults)
            )

        for Ults in InsightsObject["red_team_ults_after"]:
            self.RedUltsAfter.append(
                OWAnalytics.Ult(Ults)
            )


        #First events
        self.FirstKill  = OWAnalytics.FirstEvent(InsightsObject["first_kill"])
        self.FirstDeath = OWAnalytics.FirstEvent(InsightsObject["first_death"])
        
        #First ult can sometimes not exist
        if(InsightsObject["first_ult"] == ""):
            self.FirstUlt = None
        else:
            self.FirstUlt   = OWAnalytics.FirstEvent(InsightsObject["first_ult"])

        #Get events
        self.Events = []
        for Events in InsightsObject["events"]:
            self.Events.append(
                OWAnalytics.Event(Events)
            )

        

    def __str__(self):
        return(
            json.dumps(self.toJSON(), indent=4)
        )

    def toJSON(self):
        #Counts because some objects are too big
        BlueUltsBeforeCount = len(self.BlueUltsBefore)
        BlueUltsUsedCount = len(self.BlueUltsUsed)
        BlueUltsAfterCount = len(self.BlueUltsAfter)

        
        RedUltsBeforeCount = len(self.RedUltsBefore)
        RedUltsUsedCount = len(self.RedUltsUsed)
        RedUltsAfterCount = len(self.RedUltsAfter)

        FirstKill = {
            "Team" : self.FirstKill.Team,
            "PlayerIndex" : self.FirstKill.PlayerIndex,
            "Hero" : self.FirstKill.Hero
        }

        FirstDeath = {
            "Team" : self.FirstDeath.Team,
            "PlayerIndex" : self.FirstDeath.PlayerIndex,
            "Hero" : self.FirstDeath.Hero
        }
        
        #First ult can sometimes be none
        if(self.FirstUlt != None):
            FirstUlt = {
                "Team" : self.FirstUlt.Team,
                "PlayerIndex" : self.FirstUlt.PlayerIndex,
                "Hero" : self.FirstUlt.Hero
            }

        else:
            FirstUlt = None

        EventCount = len(self.Events)

        Object = {
            "StartTime" : self.StartTime,
            "EndTime" : self.StartTime,
            "Winner" : self.StartTime,
            "BlueHeroes" : self.StartTime,
            "RedHeroes" : self.StartTime,

            "BlueKills" : self.BlueKills,
            "BlueDeaths" : self.BlueDeaths,
            "BlueUltKills" : self.BlueUltKills,
        
            "RedKills" : self.RedKills,
            "RedDeaths" : self.RedDeaths,
            "RedUltKills" : self.RedUltKills,

            "BlueUltsBefore" : "List of {} Blue Ults Before".format(BlueUltsBeforeCount),
            "BlueUltsUsed" : "List of {} Blue Ults Used".format(BlueUltsUsedCount),
            "BlueUltsAfter" : "List of {} Blue Ults After".format(BlueUltsAfterCount),
        
            "RedUltsBefore" : "List of {} Red Ults Before".format(RedUltsBeforeCount),
            "RedUltsUsed" : "List of {} Red Ults Used".format(RedUltsUsedCount),
            "RedUltsAfter" : "List of {} Red Ults After".format(RedUltsAfterCount),

            "FirstKill" : FirstKill,
            "FirstDeath" : FirstDeath,
            "FirstUlt" : FirstUlt,

            "Events" : "List of {} Events".format(EventCount)


        }

        return Object