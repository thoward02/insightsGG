#Import insights class
import App

#Import json for dealing with json
import json

#import math for mathmatical coolness (It's a math lib... like whaddya want me to say?)
import math

#import sys and os for python functions
import sys
import os

#Setup the App object containing the class
App = App.App()

#Converts data to CSV
def ConvertToCSV():
    #Find a heros' role based on their hero | TODO: Move this... It's really odd...
    def FindRole(Hero):
        SupportList = ["lucio", "moira", "zenyatta", "brigitte", "mercy", "ana", "baptiste"]
        DpsList     = ["ashe", "bastion", "doomfist", "genji", "hanzo", "junkrat", "mccree","mei","pharah","reaper","soldier_76","sombra", "symmetra", "torbjorn", "tracer","widowmaker"]
        TankList    = ["dva","orisa","reinhardt", "roadhog", "winston", "wrecking_ball", "zarya", "sigma"]
      
        if (Hero in SupportList):
            return "support"
            
        if (Hero in DpsList):
            return "dps"
            
        if (Hero in TankList):
            return "tank"
            
    def FindBluSecondaryRole(Hero):  
        SecondaryHeroRoleList = ["maintank","offtank","hitscan","projectile","offsupport","mainsupport"]
        MainSuppList = ["lucio", "mercy"]
        OffSuppList = ["moira","zenyatta"]
        HitscanList     = ["ashe","mccree" , "reaper", "soldier_76", "widowmaker","bastion"]
        ProjList     = ["genji", "pharah", "junkrat"]
        MainTankList    = ["reinhardt", "winston", "orisa"]
        OffTankList    = ["dva", "roadhog", "zarya", "sigma"]
        
        #supports
        if Hero in BluTempSupp:
            if (Hero in MainSuppList):
                return "mainsupport"
            elif (Hero in OffSuppList):
                return "offsupport"
            elif (Hero == BluTempSupp[0]) and (BluTempSupp[1] in OffSuppList):
                return "mainsupport"
            elif (Hero == BluTempSupp[1]) and (BluTempSupp[0] in OffSuppList):
                return "mainsupport"
            elif (Hero == BluTempSupp[0]) and (BluTempSupp[1] in MainSuppList):
                return "offsupport"
            elif (Hero == BluTempSupp[1]) and (BluTempSupp[0] in MainSuppList):
                return "offsupport"
            elif (Hero == "baptiste") and (Hero == BluTempSupp[0]) and (BluTempSupp[1] == "ana"):
                return "mainsupport"
            elif (Hero == "ana") and (Hero == BluTempSupp[1]) and (BluTempSupp[0] == "baptiste"):
                return "offsupport"
            elif (Hero == "baptiste") and (Hero == BluTempSupp[1]) and (BluTempSupp[0] == "ana"):
                return "mainsupport"
            elif (Hero == "ana") and (Hero == BluTempSupp[0]) and (BluTempSupp[1] == "baptiste"):
                return "offsupport"
            elif (Hero == "baptiste") and (Hero == BluTempSupp[0]) and (BluTempSupp[1] == "lucio"):
                return "offsupport"
            elif (Hero == "brigitte") and (Hero == BluTempSupp[0]) and (BluTempSupp[1] == "lucio"):
                return "offsupport"
            elif (Hero == "baptiste") and (Hero == BluTempSupp[0]) and (BluTempSupp[1] == "brigitte"):
                return "offsupport"   
            elif (Hero == "brigitte") and (Hero == BluTempSupp[0]) and (BluTempSupp[1] == "baptiste"):
                return "mainsupport"
            elif (Hero == "baptiste") and (Hero == BluTempSupp[1]) and (BluTempSupp[0] == "brigitte"):
                return "offsupport"   
            elif (Hero == "brigitte") and (Hero == BluTempSupp[1]) and (BluTempSupp[0] == "baptiste"):
                return "mainsupport"
                
                       
        #Tanks
        if Hero in BluTempTank:
            if (Hero in MainTankList):
                return "maintank"
            elif (Hero in OffTankList):
                return "offtank"
            elif (Hero == BluTempTank[0]) and (BluTempTank[1] in OffTankList):
                return "maintank"
            elif (Hero == BluTempTank[1]) and (BluTempTank[0] in OffTankList):
                return "maintank"
            elif (Hero == BluTempTank[0]) and (BluTempTank[1] in MainTankList):
                return "offtank"
            elif (Hero == BluTempTank[1]) and (BluTempTank[0] in MainTankList):
                return "offtank"
            elif (Hero == "wrecking_ball") and (Hero == BluTempTank[0]) and (BluTempTank[1] == "winston"):
                return "offtank"  
            elif (Hero == "wrecking_ball") and (Hero == BluTempTank[1]) and (BluTempTank[0] == "winston"):
                return "offtank"
            elif (Hero == "reinhardt") and (Hero == BluTempTank[0]) and (BluTempTank[1] == "orisa"):
                return "offtank"  
            elif (Hero == "reinhardt") and (Hero == BluTempTank[1]) and (BluTempTank[0] == "orisa"):
                return "offtank"
    
        #DPS
        if Hero in BluTempDPS:
            if (Hero in HitscanList):
                return "hitscan"
            elif (Hero in ProjList):
                return "proj"
            elif (Hero == BluTempDPS[0]) and (BluTempDPS[1] in ProjList):
                return "hitscan"
            elif (Hero == BluTempDPS[1]) and (BluTempDPS[0] in ProjList):
                return "hitscan"
            elif (Hero == BluTempDPS[0]) and (BluTempDPS[1] in HitscanList):
                return "proj"
            elif (Hero == BluTempDPS[1]) and (BluTempDPS[0] in HitscanList):
                return "proj"
            elif (Hero == "hanzo") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "widowmaker"):
                return "proj"
            elif (Hero == "hanzo") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "mei"):
                return "hitscan"
            elif (Hero == "hanzo") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "mei"):
                return "hitscan"
            elif (Hero == "mei") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "hanzo"):
                return "proj"
            elif (Hero == "mei") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "hanzo"):
                return "proj"
            elif (Hero == "hanzo") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "pharah"):
                return "hitscan"
            elif (Hero == "mei") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "hanzo"):
                return "proj"
            elif (Hero == "mei") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "doomfist"):
                return "hitscan"
            elif (Hero == "doomfist") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "mei"):
                return "proj"
            elif (Hero == "mei") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "doomfist"):
                return "hitscan"
            elif (Hero == "doomfist") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "mei"):
                return "proj"   
            elif (Hero == "bastion") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "mei"):
                return "proj"
            elif (Hero == "sombra") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "tracer"):
                return "hitscan"
            elif (Hero == "tracer") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "sombra"):
                return "proj"
            elif (Hero == "sombra") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "tracer"):
                return "hitscan"
            elif (Hero == "tracer") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "sombra"):
                return "proj"
            elif (Hero == "hanzo") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "bastion"):
                return "proj"
            elif (Hero == "hanzo") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "bastion"):
                return "proj"
            elif (Hero == "mei") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "bastion"):
                return "proj"
            elif (Hero == "mei") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "bastion"):
                return "proj"
            elif (Hero == "sombra") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "hanzo"):
                return "hitscan"
            elif (Hero == "sombra") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "hanzo"):
                return "hitscan"
            elif (Hero == "hanzo") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "sombra"):
                return "proj"
            elif (Hero == "hanzo") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "sombra"):
                return "proj"
            elif (Hero == "torbjorn") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "mei"):
                return "hitscan"
            elif (Hero == "torbjorn") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "mei"):
                return "hitscan"
            elif (Hero == "mei") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "torbjorn"):
                return "proj"
            elif (Hero == "mei") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "torbjorn"):
                return "proj"
            elif (Hero == "doomfist") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "sombra"):
                return "proj"
            elif (Hero == "doomfist") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "sombra"):
                return "proj"
            elif (Hero == "sombra") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "doomfist"):
                return "hitscan"
            elif (Hero == "sombra") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "doomfist"):
                return "hitscan"
            elif (Hero == "mei") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "symmetra"):
                return "proj"
            elif (Hero == "mei") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "symmetra"):
                return "proj"
            elif (Hero == "symmetra") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "mei"):
                return "hitscan"
            elif (Hero == "symmetra") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "mei"):
                return "hitscan"
            elif (Hero == "doomfist") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "hanzo"):
                return "proj"
            elif (Hero == "doomfist") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "hanzo"):
                return "proj"
            elif (Hero == "hanzo") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "doomfist"):
                return "hitscan"
            elif (Hero == "hanzo") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "doomfist"):
                return "hitscan"
            elif (Hero == "mei") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "sombra"):
                return "proj"
            elif (Hero == "mei") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "sombra"):
                return "proj"
            elif (Hero == "sombra") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "mei"):
                return "hitscan"
            elif (Hero == "sombra") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "mei"):
                return "hitscan"
            elif (Hero == "tracer") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "mei"):
                return "hitscan"
            elif (Hero == "tracer") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "mei"):
                return "hitscan"
            elif (Hero == "mei") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "tracer"):
                return "proj"
            elif (Hero == "mei") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "tracer"):
                return "proj"
            elif (Hero == "tracer") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "hanzo"):
                return "hitscan"
            elif (Hero == "tracer") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "hanzo"):
                return "hitscan"
            elif (Hero == "hanzo") and (Hero == BluTempDPS[1]) and (BluTempDPS[0] == "tracer"):
                return "proj"
            elif (Hero == "hanzo") and (Hero == BluTempDPS[0]) and (BluTempDPS[1] == "tracer"):
                return "proj"
        return "error"

    def FindRedSecondaryRole(Hero):  
        SecondaryHeroRoleList = ["maintank","offtank","hitscan","projectile","offsupport","mainsupport"]
        MainSuppList = ["lucio", "mercy"]
        OffSuppList = ["moira","zenyatta"]
        HitscanList     = ["ashe","mccree" , "reaper", "soldier_76", "widowmaker"]
        ProjList     = ["genji", "pharah", "junkrat"]
        MainTankList    = ["reinhardt", "winston","orisa"]
        OffTankList    = ["dva", "roadhog", "zarya", "sigma"]
        
        #supports
        if Hero in RedTempSupp:
            if (Hero in MainSuppList):
                return "mainsupport"
            elif (Hero in OffSuppList):
                return "offsupport"
            elif (Hero == RedTempSupp[0]) and (RedTempSupp[1] in OffSuppList):
                return "mainsupport"
            elif (Hero == RedTempSupp[1]) and (RedTempSupp[0] in OffSuppList):
                return "mainsupport"
            elif (Hero == RedTempSupp[0]) and (RedTempSupp[1] in MainSuppList):
                return "offsupport"
            elif (Hero == RedTempSupp[1]) and (RedTempSupp[0] in MainSuppList):
                return "offsupport"
            elif (Hero == "baptiste") and (Hero == RedTempSupp[0]) and (RedTempSupp[1] == "ana"):
                return "mainsupport"
            elif (Hero == "ana") and (Hero == RedTempSupp[1]) and (RedTempSupp[0] == "baptiste"):
                return "offsupport"
            elif (Hero == "baptiste") and (Hero == RedTempSupp[1]) and (RedTempSupp[0] == "ana"):
                return "mainsupport"
            elif (Hero == "ana") and (Hero == RedTempSupp[0]) and (RedTempSupp[1] == "baptiste"):
                return "offsupport"
            elif (Hero == "baptiste") and (Hero == RedTempSupp[0]) and (RedTempSupp[1] == "lucio"):
                return "offsupport"
            elif (Hero == "brigitte") and (Hero == RedTempSupp[0]) and (RedTempSupp[1] == "lucio"):
                return "offsupport"
            elif (Hero == "baptiste") and (Hero == RedTempSupp[0]) and (RedTempSupp[1] == "brigitte"):
                return "offsupport"   
            elif (Hero == "brigitte") and (Hero == RedTempSupp[0]) and (RedTempSupp[1] == "baptiste"):
                return "mainsupport"
            elif (Hero == "baptiste") and (Hero == RedTempSupp[1]) and (RedTempSupp[0] == "brigitte"):
                return "offsupport"   
            elif (Hero == "brigitte") and (Hero == RedTempSupp[1]) and (RedTempSupp[0] == "baptiste"):
                return "mainsupport"
                
                       
        #Tanks
        if Hero in RedTempTank:
            if (Hero in MainTankList):
                return "maintank"
            elif (Hero in OffTankList):
                return "offtank"
            elif (Hero == RedTempTank[0]) and (RedTempTank[1] in OffTankList):
                return "maintank"
            elif (Hero == RedTempTank[1]) and (RedTempTank[0] in OffTankList):
                return "maintank"
            elif (Hero == RedTempTank[0]) and (RedTempTank[1] in MainTankList):
                return "offtank"
            elif (Hero == RedTempTank[1]) and (RedTempTank[0] in MainTankList):
                return "offtank"
            elif (Hero == "wrecking_ball") and (Hero == RedTempTank[0]) and (RedTempTank[1] == "winston"):
                return "offtank"
            elif (Hero == "reinhardt") and (Hero == RedTempTank[0]) and (RedTempTank[1] == "orisa"):
                return "offtank"  
            elif (Hero == "reinhardt") and (Hero == RedTempTank[1]) and (RedTempTank[0] == "orisa"):
                return "offtank"
    
        #DPS
        if Hero in RedTempDPS:
            if (Hero in HitscanList):
                return "hitscan"
            elif (Hero in ProjList):
                return "proj"
            elif (Hero == RedTempDPS[0]) and (RedTempDPS[1] in ProjList):
                return "hitscan"
            elif (Hero == RedTempDPS[1]) and (RedTempDPS[0] in ProjList):
                return "hitscan"
            elif (Hero == RedTempDPS[0]) and (RedTempDPS[1] in HitscanList):
                return "proj"
            elif (Hero == RedTempDPS[1]) and (RedTempDPS[0] in HitscanList):
                return "proj"
            elif (Hero == "hanzo") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "widowmaker"):
                return "proj"
            elif (Hero == "hanzo") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "mei"):
                return "hitscan"
            elif (Hero == "hanzo") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "mei"):
                return "hitscan"
            elif (Hero == "mei") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "hanzo"):
                return "proj"
            elif (Hero == "mei") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "hanzo"):
                return "proj"
            elif (Hero == "hanzo") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "pharah"):
                return "hitscan"
            elif (Hero == "mei") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "hanzo"):
                return "proj"
            elif (Hero == "mei") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "doomfist"):
                return "hitscan"
            elif (Hero == "doomfist") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "mei"):
                return "proj"
            elif (Hero == "mei") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "doomfist"):
                return "hitscan"
            elif (Hero == "doomfist") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "mei"):
                return "proj"   
            elif (Hero == "bastion") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "mei"):
                return "proj"
            elif (Hero == "sombra") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "tracer"):
                return "hitscan"
            elif (Hero == "tracer") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "sombra"):
                return "proj"
            elif (Hero == "sombra") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "tracer"):
                return "hitscan"
            elif (Hero == "tracer") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "sombra"):
                return "proj"
            elif (Hero == "hanzo") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "bastion"):
                return "proj"
            elif (Hero == "hanzo") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "bastion"):
                return "proj"
            elif (Hero == "mei") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "bastion"):
                return "proj"
            elif (Hero == "mei") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "bastion"):
                return "proj"
            elif (Hero == "sombra") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "hanzo"):
                return "hitscan"
            elif (Hero == "sombra") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "hanzo"):
                return "hitscan"
            elif (Hero == "hanzo") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "sombra"):
                return "proj"
            elif (Hero == "hanzo") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "sombra"):
                return "proj"
            elif (Hero == "torbjorn") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "mei"):
                return "hitscan"
            elif (Hero == "torbjorn") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "mei"):
                return "hitscan"
            elif (Hero == "mei") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "torbjorn"):
                return "proj"
            elif (Hero == "mei") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "torbjorn"):
                return "proj"
            elif (Hero == "doomfist") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "sombra"):
                return "proj"
            elif (Hero == "doomfist") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "sombra"):
                return "proj"
            elif (Hero == "sombra") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "doomfist"):
                return "hitscan"
            elif (Hero == "sombra") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "doomfist"):
                return "hitscan"
            elif (Hero == "mei") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "symmetra"):
                return "proj"
            elif (Hero == "mei") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "symmetra"):
                return "proj"
            elif (Hero == "symmetra") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "mei"):
                return "hitscan"
            elif (Hero == "symmetra") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "mei"):
                return "hitscan"
            elif (Hero == "doomfist") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "hanzo"):
                return "proj"
            elif (Hero == "doomfist") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "hanzo"):
                return "proj"
            elif (Hero == "hanzo") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "doomfist"):
                return "hitscan"
            elif (Hero == "hanzo") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "doomfist"):
                return "hitscan"
            elif (Hero == "mei") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "sombra"):
                return "proj"
            elif (Hero == "mei") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "sombra"):
                return "proj"
            elif (Hero == "sombra") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "mei"):
                return "hitscan"
            elif (Hero == "sombra") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "mei"):
                return "hitscan"
            elif (Hero == "tracer") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "mei"):
                return "hitscan"
            elif (Hero == "tracer") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "mei"):
                return "hitscan"
            elif (Hero == "mei") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "tracer"):
                return "proj"
            elif (Hero == "mei") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "tracer"):
                return "proj"
            elif (Hero == "tracer") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "hanzo"):
                return "hitscan"
            elif (Hero == "tracer") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "hanzo"):
                return "hitscan"
            elif (Hero == "hanzo") and (Hero == RedTempDPS[1]) and (RedTempDPS[0] == "tracer"):
                return "proj"
            elif (Hero == "hanzo") and (Hero == RedTempDPS[0]) and (RedTempDPS[1] == "tracer"):
                return "proj"
        return "error"            
    
    
    #Get Users teams  - Check and see if team exists, loop until right team name has been input
    print("[LOG] Here are your teams...")
    for Names in App.Teams:
        print("    [" + Names + "]")

    LoopCondition = 0;

    while LoopCondition == 0:
        TeamName      = input("What Team do you want to index?: ")

        #If user entered a viable team
        if TeamName in App.Teams:
            LoopCondition = 1

        #Else, loop until user enters team
        else:
            print("[Error] Could not find team \"" + TeamName + "\", please try again...")


    #Loop in users team, grab list of vods, and grab analysis of vods
    VodList = []
    for Vods in App.Teams[TeamName]["VodList"]:
        print("    [" + str(len(VodList)) + "]: " + Vods)
        VodList.append(Vods)

    #Ask user what vod they want
    print("[LOG] Which one do you wanna fetch the analysis for?")

    Analyze = int(input("Vod Num: "))

    #Fetch the analysis for that vod
    RawMatchList = App.Teams[TeamName]["VodList"][VodList[Analyze]]["latestAnalysis"]["result"]["matches"]
    IdList   = []

    for Matches in RawMatchList:
        IdList.append(Matches["id"])

    print("[LOG] Grabbing analytics from " + str(VodList[Analyze]))

    #Send of match id list to be read
    MatchAnalytics = App.GrabAnalytics(IdList)

    #Create a custom CSV based on what we want
    CSVOutput = "Map ,Stage, Start, End, Duration, Winner, BTank 1, BTank 2, BDps 1, BDps 2, BSupport 1, BSupport 2, RTank 1, RTank 2, RDps 1, RDps 2, RSupport 1, RSupport 2, BTank 1 Before Ult %, BTank 2 Before Ult %, BDps 1 Before Ult %, BDps 2 Before Ult %, BSupport 1 Before Ult %, BSupport 2 Before Ult %, RTank 1 Before Ult %, RTank 2 Before Ult %, RDps 1 Before Ult %, RDps 2 Before Ult %, RSupport 1 Before Ult %, RSupport 2 Before Ult %, BTank 1 Ult Usage, BTank 2 Ult Usage, BDps 1 Ult Usage, BDps 2 Ult Usage, BSupport 1 Ult Usage, BSupport 2 Ult Usage, RTank 1 Ult Usage, RTank 2 Ult Usage, RDps 1 Ult Usage, RDps 2 Ult Usage, RSupport 1 Ult Usage, RSupport 2 Ult Usage, Total Blue Ults, Total Red Ults, BTank 1 After Ult %, BTank 2 After Ult %, BDps 1 After Ult %, BDps 2 After Ult %, BSupport 1 After Ult %, BSupport 2 After Ult %, RTank 1 After Ult %, RTank 2 After Ult %, RDps 1 After Ult %, RDps 2 After Ult %, RSupport 1 After Ult %, RSupport 2 After Ult %, First Ult Team, First Ult Caster, First Kill Team, First Kill Killer, First Kill Killie, Blue Kills, Red Kills, Blue MT Kills, Blue MT Deaths, Blue OT Kills, Blue OT Deaths, Blue HS Kills, Blue HS Deaths, Blue Proj Kills, Blue Proj Deaths, Blue FS Kills, Blue FS Deaths, Blue MS Kills, Blue MS Deaths, Red MT Kills, Red MT Deaths, Red OT Kills, Red OT Deaths, Red HS Kills, Red HS Deaths, Red Proj Kills, Red Proj Deaths, Red FS Kills, Red FS Deaths, Red MS Kills, Red MS Deaths,  "

    print("[LOG] Sorting matches...")
    #For each match analyzed
    
    for MatchUps in MatchAnalytics["matches"]:
        
        #For each fight in match
        for TeamFights in MatchUps["data"]["teamfights"]:
            #Setup heroes
            BLUEHEROES = ""
            REDHEROES  = ""

            roles      = ["maintank","offtank","hitscan", "proj","offsupport", "mainsupport"]
            BluTempSupp = []
            BluTempDPS = []
            BluTempTank = []
            RedTempSupp = []
            RedTempDPS = []
            RedTempTank = []
            
            BluMainTank = ""
            BluOffTank = ""
            BluHitscan = ""
            BluProj = ""
            BluMainSupp = ""
            BluOffSupp = ""
            
            RedMainTank = ""
            RedOffTank = ""
            RedHitscan = ""
            RedProj = ""
            RedMainSupp = ""
            RedOffSupp = ""

            BluTemp    = []
            RedTemp    = []

            #Find ults used this fight
            BlueTempUltUsage = []
            RedTempUltUsage  = []

            BluUltUsage      = [0, 0, 0, 0, 0, 0]
            RedUltUsage      = [0, 0, 0, 0, 0, 0]
            
            for Ults in TeamFights["blue_team_ults_used"]:
                BlueTempUltUsage.append(Ults["hero"])

            for Ults in TeamFights["red_team_ults_used"]:
                RedTempUltUsage.append(Ults["hero"])

            #Easy organization of teams
            #Seperate teams into character type
            for Hero in TeamFights["blue_heroes"]:
                if(FindRole(Hero) == "support"):
                    BluTempSupp.append(Hero)
                elif(FindRole(Hero) == "tank"):
                    BluTempTank.append(Hero)
                elif(FindRole(Hero) == "dps"):
                        BluTempDPS.append(Hero)

            for Hero in TeamFights["red_heroes"]:
                if(FindRole(Hero) == "support"):
                    RedTempSupp.append(Hero)
                elif(FindRole(Hero) == "tank"):
                    RedTempTank.append(Hero)
                elif(FindRole(Hero) == "dps"):
                    RedTempDPS.append(Hero)
            
            #Seperate Heros in each character type into roles
            for Role in roles:
                for Hero in BluTempSupp:
                    if(FindBluSecondaryRole(Hero) == Role):
                        BluTemp.append(Hero)
                        if Role == "mainsupport":
                            BluMainSupp = Hero
                        elif Role == "offsupport":
                            BluOffSupp = Hero
                for Hero in BluTempTank:
                    if(FindBluSecondaryRole(Hero) == Role):
                        BluTemp.append(Hero)
                        if Role == "maintank":
                            BluMainTank = Hero
                        elif Role == "offtank":
                            BluOffTank = Hero  
                for Hero in BluTempDPS:
                    if(FindBluSecondaryRole(Hero) == Role):
                        BluTemp.append(Hero)
                        if Role == "hitscan":
                            BluHitscan = Hero
                        elif Role == "proj":
                            BluProj = Hero
                for Hero in RedTempSupp:
                    if(FindRedSecondaryRole(Hero) == Role):
                        RedTemp.append(Hero)
                        if Role == "mainsupport":
                            RedMainSupp = Hero
                        elif Role == "offsupport":
                            RedOffSupp = Hero
                for Hero in RedTempTank:
                    if(FindRedSecondaryRole(Hero) == Role):
                        RedTemp.append(Hero)
                        if Role == "maintank":
                            RedMainTank = Hero
                        elif Role == "offtank":
                            RedOffTank = Hero
                for Hero in RedTempDPS:
                    if(FindRedSecondaryRole(Hero) == Role):                  
                        RedTemp.append(Hero)
                        if Role == "hitscan":
                            RedHitscan = Hero
                        elif Role == "proj":
                            RedProj = Hero
                                    
            #CSV Format Heroes - Sort through the Heroes, organize them for CSV, and flag which one ulted
            Counter = 0
            for Heroes in BluTemp:
                if Heroes in BlueTempUltUsage:
                    BluUltUsage[Counter] = 1
                BLUEHEROES += Heroes + ", "
                Counter += 1

            Counter = 0

            for Heroes in RedTemp:
                if Heroes in RedTempUltUsage:
                    RedUltUsage[Counter] = 1
                REDHEROES += Heroes + ", "
                Counter += 1
    
            #Fetch Ults
            BlueUltBefore = ""
            for Ults in TeamFights["blue_team_ults_before"]:
                if(Ults["status"] == "ready"):
                    Ults["status"] = "100"
                BlueUltBefore += str(Ults["status"]) + ","


            RedUltBefore  = ""
            for Ults in TeamFights["red_team_ults_before"]:
                if(Ults["status"] == "ready"):
                    Ults["status"] = "100"
                RedUltBefore += str(Ults["status"]) + ","


            BlueUltAfter = ""
            for Ults in TeamFights["blue_team_ults_after"]:
                if(Ults["status"] == "ready"):
                    Ults["status"] = "100"
                BlueUltAfter +=  str(Ults["status"]) + ","


            RedUltAfter  = ""
            for Ults in TeamFights["red_team_ults_after"]:
                if(Ults["status"] == "ready"):
                    Ults["status"] = "100"
                RedUltAfter += str(Ults["status"]) + ","

            #Ults used
            BlueUltsUsed = ""
            RedUltsUsed  = ""
            
            #Total up the number
            TotalUltsBlu = sum(BluUltUsage)
            TotalUltsRed = sum(RedUltUsage)
            
            for Ults in BluUltUsage:
                BlueUltsUsed += str(Ults) + ", "


            for Ults in RedUltUsage:
                RedUltsUsed += str(Ults) + ", "

            #Ults - If there were first ults used, port them over
            if(TeamFights["first_ult"] != ""):
                FirstUltTeam    = TeamFights["first_ult"]["team"]
                FirstUltTarget  = TeamFights["first_ult"]["hero"]
            else:
                FirstUltTeam    = "Null"
                FirstUltTarget  = "Null"

            #Kills - If there were kills, port them over
            if(TeamFights["first_kill"] != ""):
                FirstKillTeam   = TeamFights["first_kill"]["team"]
                FirstKillTarget = TeamFights["first_death"]["hero"]
                FirstKillKiller = TeamFights["first_kill"]["hero"]
            else:
                FirstKillTeam   = "Null"
                FirstKillTarget = "Null"
                FirstKillKiller = "Null"

            #Check and assign the map and stage for KOTH    
            map = ""
            stage = ""
            
            if "hanamura" in str(MatchUps["data"]["map"]):
                map = "Hanamura"
            if "lunar" in str(MatchUps["data"]["map"]):
                map = "Lunar" 
            if "temple" in str(MatchUps["data"]["map"]):
                map = "Temple of Anubis"
            if "volskaya" in str(MatchUps["data"]["map"]):
                map = "Volskaya" 
            if "paris" in str(MatchUps["data"]["map"]):
                map = "Paris"
            if "dorado" in str(MatchUps["data"]["map"]):
                map = "Dorado" 
            if "junkertown" in str(MatchUps["data"]["map"]):
                map = "Junkertown"
            if "rialto" in str(MatchUps["data"]["map"]):
                map = "Rialto"
            if "route" in str(MatchUps["data"]["map"]):
                map = "Route 66"
            if "gibraltar" in str(MatchUps["data"]["map"]):
                map = "Gibraltar" 
            if "havana" in str(MatchUps["data"]["map"]):
                map = "Havana"
            if "blizz" in str(MatchUps["data"]["map"]):
                map = "Blizzard World" 
            if "eichen" in str(MatchUps["data"]["map"]):
                map = "Eichenwalde"
            if "hollywood" in str(MatchUps["data"]["map"]):
                map = "Hollywood" 
            if "kings" in str(MatchUps["data"]["map"]):
                map = "King's Row"
            if "numbani" in str(MatchUps["data"]["map"]):
                map = "Numbani"
            
            #Assigning the stage for KOTH
            if "lijiang" in str(MatchUps["data"]["map"]):
                map = "Lijiang" 
                if "arket" in str(MatchUps["data"]["map"]):
                    stage = "Night Market"
                if "arden" in str(MatchUps["data"]["map"]):
                    stage = "Gardens"
                if "ontrol" in str(MatchUps["data"]["map"]):
                    stage = "Control Center"
            if "oasis" in str(MatchUps["data"]["map"]):
                map = "Oasis" 
                if "ity" in str(MatchUps["data"]["map"]):
                    stage = "City Center"
                if "arden" in str(MatchUps["data"]["map"]):
                    stage = "Gardens"
                if "niversity" in str(MatchUps["data"]["map"]):
                    stage = "University"
            if "ilios" in str(MatchUps["data"]["map"]):
                map = "Illios" 
                if "uin" in str(MatchUps["data"]["map"]):
                    stage = "Ruins"
                if "ell" in str(MatchUps["data"]["map"]):
                    stage = "Well"
                if "ight" in str(MatchUps["data"]["map"]):
                    stage = "Lighthouse" 
            if "nepal" in str(MatchUps["data"]["map"]):
                map = "Nepal" 
                if "illage" in str(MatchUps["data"]["map"]):
                    stage = "Village"
                if "hrine" in str(MatchUps["data"]["map"]):
                    stage = "Shrine"
                if "anctum" in str(MatchUps["data"]["map"]):
                    stage = "Sanctum"
            if "busan" in str(MatchUps["data"]["map"]):
                map = "Busan" 
                if "own" in str(MatchUps["data"]["map"]):
                    stage = "Downtown"
                if "eka" in str(MatchUps["data"]["map"]):
                    stage = "Mekabase"
                if "anct" in str(MatchUps["data"]["map"]):
                    stage = "Sanctuary" 
            
            #killcount
            BluMainTankKills = 0
            BluOffTankKills = 0
            BluHitscanKills = 0
            BluProjKills = 0
            BluMainSuppKills = 0
            BluOffSuppKills = 0
            
            RedMainTankKills = 0
            RedOffTankKills = 0
            RedHitscanKills = 0
            RedProjKills = 0
            RedMainSuppKills = 0
            RedOffSuppKills = 0
            
            #deathcount
            BluMainTankDeaths = 0
            BluOffTankDeaths = 0
            BluHitscanDeaths = 0
            BluProjDeaths = 0
            BluMainSuppDeaths = 0
            BluOffSuppDeaths = 0
            
            RedMainTankDeaths = 0
            RedOffTankDeaths = 0
            RedHitscanDeaths = 0
            RedProjDeaths = 0
            RedMainSuppDeaths = 0
            RedOffSuppDeaths = 0
            
            #Count deaths/kills of individuals in each fight
            for KillBlocks in MatchUps["data"]["kills"]:
                if KillBlocks["start_time"] >= TeamFights["start_time"] and KillBlocks["start_time"] <= TeamFights["end_time"]:  
                    #Setup Killer
                    Killer      = KillBlocks["killer"]["hero"]
                    KillerTeam  = KillBlocks["killer"]["color"]
            
                    #Target
                    Target      = KillBlocks["killee"]["hero"]

                    #BlueTeam                    
                    #kills
                    if KillBlocks["ability"] != "resurrect":
                        if KillerTeam == "blue":
                            if Killer == BluMainTank:
                                BluMainTankKills +=1
                            if Killer == BluOffTank:
                                BluOffTankKills +=1
                            if Killer == BluHitscan:
                                BluHitscanKills +=1
                            if Killer == BluProj:
                                BluProjKills +=1
                            if Killer == BluMainSupp:
                                BluMainSuppKills +=1
                            if Killer == BluOffSupp:
                                BluOffSuppKills +=1
                            #Killees
                            if Target == RedMainTank:
                                RedMainTankDeaths +=1
                            if Target == RedOffTank:
                                RedOffTankDeaths +=1
                            if Target == RedHitscan:
                                RedHitscanDeaths +=1
                            if Target == RedProj:
                                RedProjDeaths +=1
                            if Target == RedMainSupp:
                                RedMainSuppDeaths +=1
                            if Target == RedOffSupp:
                                RedOffSuppDeaths +=1
        
                        #RedTeam
                        #kills
                        if KillerTeam == "red":
                            if Killer == RedMainTank:
                                RedMainTankKills +=1
                            if Killer == RedOffTank:
                                RedOffTankKills +=1
                            if Killer == RedHitscan:
                                RedHitscanKills +=1
                            if Killer == RedProj:
                                RedProjKills +=1
                            if Killer == RedMainSupp:
                                RedMainSuppKills +=1
                            if Killer == RedOffSupp:
                                RedOffSuppKills +=1  
                            #killees
                            if Target == BluMainTank:
                                BluMainTankDeaths +=1
                            if Target == BluOffTank:
                                BluOffTankDeaths +=1
                            if Target == BluHitscan:
                                BluHitscanDeaths +=1
                            if Target == BluProj:
                                BluProjDeaths +=1
                            if Target == BluMainSupp:
                                BluMainSuppDeaths +=1
                            if Target == BluOffSupp:
                                BluOffSuppDeaths +=1
                            
            #Output - TODO, Clean this holy fuck it's messy dude
            CSVOutput += "\n" + map + "," + stage + "," + str(int(TeamFights["start_time"])) + "," + str(int(TeamFights["end_time"])) + "," + str(int(TeamFights["end_time"] - TeamFights["start_time"])) + "," + TeamFights["winner"]  + "," + BLUEHEROES + REDHEROES + BlueUltBefore + RedUltBefore + BlueUltsUsed +  RedUltsUsed + str(TotalUltsBlu) + "," + str(TotalUltsRed) + "," +  BlueUltAfter + RedUltAfter + FirstUltTeam + "," + FirstUltTarget + "," + FirstKillTeam + "," + FirstKillKiller + "," + FirstKillTarget + "," + str(TeamFights["blue_team_kills"]) + "," + str(TeamFights["red_team_kills"]) + "," + str(BluMainTankKills) + "," + str(BluMainTankDeaths) + "," + str(BluOffTankKills) + "," + str(BluOffTankDeaths) + "," + str(BluHitscanKills) + "," + str(BluHitscanDeaths)+ "," + str(BluProjKills) + "," + str(BluProjDeaths) + "," + str(BluMainSuppKills) + "," + str(BluMainSuppDeaths) + "," + str(BluOffSuppKills) + "," + str(BluOffSuppDeaths) + "," + str(RedMainTankKills) + "," + str(RedMainTankDeaths) + "," + str(RedOffTankKills) + "," + str(RedOffTankDeaths) + "," + str(RedHitscanKills) + "," + str(RedHitscanDeaths)+ "," + str(RedProjKills) + "," + str(RedProjDeaths) + "," + str(RedMainSuppKills) + "," + str(RedMainSuppDeaths) + "," + str(RedOffSuppKills) + "," + str(RedOffSuppDeaths)

            
    print("[LOG] Done sorting")

    FileName = input("What would you like to save the file name as?: ")
    #Push the output
    with open("Outputs/" + FileName + ".csv", "w") as OutputFile:
        OutputFile.write(CSVOutput)

    print("[LOG] Done! Exiting")


#Starting Point
def Start():
    #Welcome lol
    print(" -- Welcome to the Example CSV Report -- ")

    #Check for cred
    Username = None
    Password = None

    #Check to see if user included login information in start (Uh this won't work if they have a space in their username or password, but I don't feel like fixing it...)
    if len(sys.argv) == 3:
        Username = sys.argv[1]
        Password = sys.argv[2]

    #If they didn't put their username and password in as parameters, check and see if they've got a login.json
    elif os.path.exists("Login.json"):
        #Grab user info from file
        try:
            with open("Login.json") as LoginFile:
                LoginInfo = json.load(LoginFile)
        except:
            raise ValueError("[Error] Could not read login.json")

        #Check to see if username and password dicts are there
        if "username" in LoginInfo and "password" in LoginInfo:
            Username = LoginInfo["username"]
            Password = LoginInfo["password"]
        #If username | password doesn't exist, toss an error
        else:
            raise ValueError("[Error] Couldn't find the username or password in login.json, check to see if you formatted it correctly")

    else:
        raise ValueError("[Error] Did not get a username and password to work with... Check the README and ensure you're following the instructions.")

    #Login - If the code made it this far, then there are some creds to login with
    print("[LOG] Logging in... ")
    App.Login(Username, Password)
    print("[LOG] Logged in. ")

    #Start the user task
    ConvertToCSV()



Start()
