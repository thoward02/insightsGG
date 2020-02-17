"""
    File: insightsGG/Objects/Team.py
    Author: Aud#9488
    Desc: This file contains the class for creating insights me objects, where
          Me is the current user logged in
"""

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
            return "UserObject:\n\tId : {},\n\tName : {},\n\tEmail : {},\n\tNickname : {},\n\tProfilePicture : {},\n\tVerified : {},\n\tWhiteListed : {},\n\tMarketing : {},\n\tUpdates : {}\n\t    ".format(self.Id, self.Name, self.Email, self.Nickname, self.ProfilePicture, self.ProfilePicture, self.Verified, self.WhiteListed, self.Marketing, self.Updates)
