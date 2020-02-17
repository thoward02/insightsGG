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
