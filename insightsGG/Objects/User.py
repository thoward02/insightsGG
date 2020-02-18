"""
    File: insightsGG/Objects/User.py
    Author: Aud#9488
    Desc: This file contains the class for creating insights user objects
"""
#import json for pretty print
import json

class User:
    def __init__(self, InsightsUser):
        self.Id             = InsightsUser["id"]
        self.Nickname       = InsightsUser["alias"]
        self.ProfilePicture = InsightsUser["picture"]



    #Create custom print out
    def __str__(self):
        return json.dumps(self.toJSON(), indent=4, sort_keys=False)


    #Create custom json output
    def toJSON(self):
        Object = {
            "Id"             : self.Id,
            "Nickname"       : self.Nickname,
            "ProfilePicture" : self.ProfilePicture
        }

        return Object
