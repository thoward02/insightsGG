"""
    File: insightsGG/Objects/Video.py
    Author: Aud#9488
    Desc: This file contains the class for creating insights Video objects
"""

class Video:
    def __init__(self, InsightsVideo):
        #Setup identifications
        self.Id            = InsightsVideo["id"]
        self.Name          = InsightsVideo["name"]
        self.Tags          = InsightsVideo["tags"]

        #Setup VOD metadata
        self.VodLink       = InsightsVideo["remoteUrl"]
        self.StreamLink    = InsightsVideo["streamUrl"]
        self.CreationDate  = InsightsVideo["created"]
        self.Length        = InsightsVideo["duration"]
        self.TeamOwnerId   = InsightsVideo["owner"]["id"]

        self.Thumbnail     = InsightsVideo["thumbnail"]
        self.Uploaded      = InsightsVideo["uploaded"]

        self.AllowComments = InsightsVideo["comments"]

        #Setup analysis
        if(InsightsVideo["latestAnalysis"] != None) and (InsightsVideo["latestAnalysis"]["error"] == None):
            self.Analysis      = True
            self.AnalysisError = False
            self.AnalysisIds   = InsightsVideo["latestAnalysis"]["result"]["matches"]

        #If analysis, but failed
        if(InsightsVideo["latestAnalysis"] != None) and (InsightsVideo["latestAnalysis"]["error"] != None):
            self.Analysis      = True
            self.AnalysisError = True
            self.AnalysisIds   = []


        #If no analysis
        if(InsightsVideo["latestAnalysis"] == None):
            self.Analysis      = False
            self.AnalysisError = False
            self.AnalysisIds   = []
