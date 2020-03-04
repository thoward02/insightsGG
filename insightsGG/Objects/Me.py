"""
    File: insightsGG/Objects/Me.py
    Author: Aud#9488
    Desc: This file contains the class for creating insights me objects, where
          Me is the current user logged in
"""
#import json for pretty print
import json

#Import Libs
from .User import User

class Me(User):
    def __init__(self, InsightsUser):
        #Fill in orginal data
        super().__init__(InsightsUser)

        #Fill up new data
        self.Name        = InsightsUser["name"]
        self.Email       = InsightsUser["email"]
        self.Verfied     = InsightsUser["verified"]
        self.WhiteListed = InsightsUser["whitelisted"]
        self.Marketing   = InsightsUser["marketing"]
        self.Updates     = InsightsUser["updates"]



    #Create custom print out
    def __str__(self):
        return json.dumps(self.toJSON(), indent=4, sort_keys=False)


    #Create custom json output
    def toJSON(self):
        Object = {
            "Id"             : self.Id,
            "Name"           : self.Name,
            "Nickname"       : self.Nickname,
            "Email"          : self.Email,
            "ProfilePicture" : self.ProfilePicture,
            "WhiteListed"    : self.WhiteListed,
            "Marketing"      : self.Marketing,
            "Updates"        : self.Updates,
        }

        return Object
