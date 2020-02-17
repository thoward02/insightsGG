"""
    File: insightsGG/Objects/User.py
    Author: Aud#9488
    Desc: This file contains the class for creating insights user objects
"""

class User:
    def __init__(self, InsightsUser):
        self.Id             = InsightsUser["id"]
        self.Nickname       = InsightsUser["alias"]
        self.ProfilePicture = InsightsUser["picture"]



    #Create custom print out
    def __str__(self):
        return "UserObject:\n\tId : {},\n\tNickname : {},\n\tProfilePicture : {}".format(self.Id, self.Nickname, self.ProfilePicture)
