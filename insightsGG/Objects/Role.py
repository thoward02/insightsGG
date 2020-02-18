"""
    File: insightsGG/Objects/Role.py
    Author: Aud#9488
    Desc: This file contains the class for creating insights role objects
"""

class Role:
    def __init__(self, InsightsRole):
        #Setup identification
        self.Id             = InsightsRole["id"]
        self.Name           = InsightsRole["name"]

        #Setup meta data
        self.Privileges     = InsightsRole["privileges"]
        self.Global         = InsightsRole["global"] #wtf is this?


    """
        == Functions that help the user ==
    """
    def __str__(self):
        return json.dumps(self.toJSON(), indent=4, sort_keys=False)

    def toJSON(self):
        PrettyPrinted = {
            "Id"          : self.Id,
            "Name"        : self.Name,
            "Privileges"  : self.Privileges,
            "Global"      : self.Global
        }

        return PrettyPrinted
