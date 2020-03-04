"""
    File: insightsGG/Objects/Video.py
    Author: Aud#9488
    Desc: This file contains the class for creating insights Video objects
"""
#import json for pretty print
import json

#Import self libraries
import insightsGG.Objects
import insightsGG.Errors  as Errors


class Video:
    def __init__(self, *args, **kwargs):
        #Setup parent class
        self.ParentClass   = kwargs.get("ParentClass")
        InsightsVideo      = kwargs.get("InsightsObject")

        if InsightsVideo == None:
            raise Errors.VideoError.MissingArgumentError("Missing InsightsObject argument")

        if self.ParentClass == None:
            raise Errors.VideoError.MissingArgumentError("Missing ParentClass argument")

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
        self.Public        = InsightsVideo["public"]

        #Setup analysis
        if(InsightsVideo["latestAnalysis"] != None) and (InsightsVideo["latestAnalysis"]["error"] == None):
            self.Analysis      = True
            self.AnalysisError = False

            #Log ids
            self.AnalysisIds = []
            for Ids in InsightsVideo["latestAnalysis"]["result"]["matches"]:
                self.AnalysisIds.append(Ids["id"])

        #If analysis, but failed
        elif(InsightsVideo["latestAnalysis"] != None) and (InsightsVideo["latestAnalysis"]["error"] != None):
            self.Analysis      = True
            self.AnalysisError = True
            self.AnalysisIds   = []


        #If no analysis
        elif(InsightsVideo["latestAnalysis"] == None):
            self.Analysis      = False
            self.AnalysisError = False
            self.AnalysisIds   = []


    """
        == Functions to grab data ==
    """
    #Grab the tags on a video
    def GrabTags(self):
        #Fetch tag list
        TeamTagList = self.ParentClass.GetTags(self.TeamOwnerId, 100)

        #Create tag objects for ever tag list
        ReturnTagList = []
        for Tags in TeamTagList:
            if(Tags["id"] in self.Tags):
                ReturnTagList.append(insightsGG.Objects.Tag(Tags))

        return ReturnTagList

    #Delete a video
    def Delete(self):
        self.ParentClass.DeleteVod(self.Id)

    #Analyze Vod
    def Analyze(self):
        return self.ParentClass.RequestOverwatchAnalysis(self.Id)

    #Fetch Analysis
    def FetchAnalysis(self):
        if self.Analysis == True:
            return self.ParentClass.GrabAnalytics(self.AnalysisIds)

        if self.Analysis == False:
            raise Errors.VideoError.VodNotAnalyzed("No analysis found")

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
            "Tags"          : self.Tags,
            "VodLink"       : self.VodLink,
            "StreamLink"    : self.StreamLink,
            "CreationDate"  : self.CreationDate,
            "Length"        : self.Length,
            "TeamOwnerId"   : self.TeamOwnerId,
            "Thumbnail"     : self.Thumbnail,
            "Uploaded"      : self.Uploaded,
            "AllowComments" : self.AllowComments,
            "Public"        : self.Public
        }

        return PrettyPrinted
