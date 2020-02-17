"""
    File: insightsGG/Objects/Team.py
    Author: Aud#9488
    Desc: This file contains the class for creating insights Team objects
"""

import insightsGG.Objects
import insightsGG
class Team:
    def __init__(self, ParentClass, InsightsTeam):
        #Setup reference to parent class
        self.Parent = ParentClass

        #Setup identifications
        self.Id      = InsightsTeam["team"]["id"]
        self.Name    = InsightsTeam["team"]["name"]

        #Setup meta data
        self.Picture     = InsightsTeam["team"]["picture"]
        self.Description = InsightsTeam["team"]["description"]
        self.Owner       = insightsGG.Objects.User(InsightsTeam["team"]["owner"])

        #Setup team specifics
        self.Privileges = InsightsTeam["privileges"] #wtf is this?
        self.Roles      = []

        #Push in roles
        for Roles in InsightsTeam["roles"]:
            self.Roles.append(insightsGG.Objects.Role(Roles))



    def GetVideos(self):
        return self.Parent.GrabTeamVodList(self.Id, 100)
