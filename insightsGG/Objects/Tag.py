"""
    File: insightsGG/Objects/Tag.py
    Author: Aud#9488
    Desc: This file contains the class for creating insights Tag objects
"""
#import json for pretty print
import json

#Import self libraries
import insightsGG.Objects


class Tag:
    def __init__(self, InsightsVideo):
        #Setup identifications
        self.Id            = InsightsVideo["id"]
        self.Name          = InsightsVideo["name"]
        self.Colour        = InsightsVideo["color"]

    """
        == Functions that help the user ==
    """
    #Add custom print out
    def __str__(self):
        PrettyPrinted = self.toJSON()

        return json.dumps(PrettyPrinted, indent=4, sort_keys=False)


    #Add Custom JSON
    def toJSON(self):
        PrettyPrinted = {
            "Id"            : self.Id,
            "Name"          : self.Name,
            "Colour"        : self.Colour
        }

        return PrettyPrinted
