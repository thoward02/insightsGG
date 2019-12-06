#Import insights class
import insightsGG

#Import json for dealing with json
import json

#import math for mathmatical coolness (It's a math lib... like whaddya want me to say?)
import math

#import sys and os for python functions
import sys
import os


#Create the data scrubber class (Contains functions too big to contain below)
class DataCleaner:
    #Find a heros' role based on their hero
    def FindRole(self, Hero):
        SupportList = ["lucio", "moira", "zenyatta", "brigitte", "mercy", "ana", "baptiste"]
        DpsList     = ["ashe", "bastion", "doomfist", "genji", "hanzo", "junkrat", "mccree","mei","pharah","reaper","soldier_76","sombra", "symmetra", "torbjorn", "tracer","widowmaker"]
        TankList    = ["dva","orisa","reinhardt", "roadhog", "winston", "wrecking_ball", "zarya", "sigma"]

        if (Hero in SupportList):
            return "support"

        if (Hero in DpsList):
            return "dps"

        if (Hero in TankList):
            return "tank"

    #Find red's secondary role
    def FindSecondaryRole(self, Hero, TempSupp, TempTank, TempDPS):
        SecondaryHeroRoleList = ["maintank","offtank","hitscan","projectile","offsupport","mainsupport"]
        MainSuppList = ["lucio", "mercy"]
        OffSuppList = ["moira","zenyatta"]
        HitscanList     = ["ashe","mccree" , "reaper", "soldier_76", "widowmaker"]
        ProjList     = ["genji", "pharah", "junkrat"]
        MainTankList    = ["reinhardt", "winston","orisa"]
        OffTankList    = ["dva", "roadhog", "zarya", "sigma"]

        #supports
        if Hero in TempSupp:
            if (Hero == "baptiste") and (Hero == TempSupp[0]) and (TempSupp[1] == "ana"):
                return "mainsupport"
            elif (Hero == "ana") and (Hero == TempSupp[1]) and (TempSupp[0] == "baptiste"):
                return "offsupport"
            elif (Hero == "baptiste") and (Hero == TempSupp[1]) and (TempSupp[0] == "ana"):
                return "mainsupport"
            elif (Hero == "ana") and (Hero == TempSupp[0]) and (TempSupp[1] == "baptiste"):
                return "offsupport"
            elif (Hero == "baptiste") and (Hero == TempSupp[0]) and (TempSupp[1] == "lucio"):
                return "offsupport"
            elif (Hero == "brigitte") and (Hero == TempSupp[0]) and (TempSupp[1] == "lucio"):
                return "offsupport"
            elif (Hero == "baptiste") and (Hero == TempSupp[0]) and (TempSupp[1] == "brigitte"):
                return "offsupport"
            elif (Hero == "brigitte") and (Hero == TempSupp[0]) and (TempSupp[1] == "baptiste"):
                return "mainsupport"
            elif (Hero == "baptiste") and (Hero == TempSupp[1]) and (TempSupp[0] == "brigitte"):
                return "offsupport"
            elif (Hero == "brigitte") and (Hero == TempSupp[1]) and (TempSupp[0] == "baptiste"):
                return "mainsupport"
            elif (Hero == "mercy") and (Hero == TempSupp[0]) and (TempSupp[1] == "lucio"):
                return "mainsupport"
            elif (Hero == "mercy") and (Hero == TempSupp[0]) and (TempSupp[1] == "lucio"):
                return "mainsupport"
            elif (Hero == "lucio") and (Hero == TempSupp[0]) and (TempSupp[1] == "mercy"):
                return "offsupport"
            elif (Hero == "lucio") and (Hero == TempSupp[1]) and (TempSupp[0] == "mercy"):
                return "offsupport"
            elif (Hero in MainSuppList):
                return "mainsupport"
            elif (Hero in OffSuppList):
                return "offsupport"
            elif (Hero == TempSupp[0]) and (TempSupp[1] in OffSuppList):
                return "mainsupport"
            elif (Hero == TempSupp[1]) and (TempSupp[0] in OffSuppList):
                return "mainsupport"
            elif (Hero == TempSupp[0]) and (TempSupp[1] in MainSuppList):
                return "offsupport"
            elif (Hero == TempSupp[1]) and (TempSupp[0] in MainSuppList):
                return "offsupport"

        #Tanks
        if Hero in TempTank:
            if (Hero == "wrecking_ball") and (Hero == TempTank[0]) and (TempTank[1] == "winston"):
                return "offtank"
            elif (Hero == "wrecking_ball") and (Hero == TempTank[1]) and (TempTank[0] == "winston"):
                return "offtank"
            elif (Hero == "orisa") and (Hero == TempTank[0]) and (TempTank[1] == "wrecking_ball"):
                return "maintank"
            elif (Hero == "orisa") and (Hero == TempTank[1]) and (TempTank[0] == "wrecking_ball"):
                return "maintank"
            elif (Hero == "wrecking_ball") and (Hero == TempTank[0]) and (TempTank[1] == "orisa"):
                return "offtank"
            elif (Hero == "wrecking_ball") and (Hero == TempTank[1]) and (TempTank[0] == "orisa"):
                return "offtank"
            elif (Hero == "reinhardt") and (Hero == TempTank[0]) and (TempTank[1] == "orisa"):
                return "offtank"
            elif (Hero == "reinhardt") and (Hero == TempTank[1]) and (TempTank[0] == "orisa"):
                return "offtank"
            elif (Hero == "orisa") and (Hero == TempTank[0]) and (TempTank[1] == "reinhardt"):
                return "maintank"
            elif (Hero == "orisa") and (Hero == TempTank[1]) and (TempTank[0] == "reinhardt"):
                return "maintank"
            elif (Hero == "reinhardt") and (Hero == TempTank[0]) and (TempTank[1] == "orisa"):
                return "offtank"
            elif (Hero == "reinhardt") and (Hero == TempTank[1]) and (TempTank[0] == "orisa"):
                return "offtank"
            elif (Hero == "orisa") and (Hero == TempTank[0]) and (TempTank[1] == "winston"):
                return "maintank"
            elif (Hero == "orisa") and (Hero == TempTank[1]) and (TempTank[0] == "winston"):
                return "maintank"
            elif (Hero == "winston") and (Hero == TempTank[0]) and (TempTank[1] == "orisa"):
                return "offtank"
            elif (Hero == "winston") and (Hero == TempTank[1]) and (TempTank[0] == "orisa"):
                return "offtank"
            elif (Hero in MainTankList):
                return "maintank"
            elif (Hero in OffTankList):
                return "offtank"
            elif (Hero == TempTank[0]) and (TempTank[1] in OffTankList):
                return "maintank"
            elif (Hero == TempTank[1]) and (TempTank[0] in OffTankList):
                return "maintank"
            elif (Hero == TempTank[0]) and (TempTank[1] in MainTankList):
                return "offtank"
            elif (Hero == TempTank[1]) and (TempTank[0] in MainTankList):
                return "offtank"

        #DPS
        if Hero in TempDPS:
            if (Hero == "hanzo") and (Hero == TempDPS[0]) and (TempDPS[1] == "widowmaker"):
                return "proj"
            elif (Hero == "hanzo") and (Hero == TempDPS[0]) and (TempDPS[1] == "mei"):
                return "hitscan"
            elif (Hero == "hanzo") and (Hero == TempDPS[1]) and (TempDPS[0] == "mei"):
                return "hitscan"
            elif (Hero == "mei") and (Hero == TempDPS[0]) and (TempDPS[1] == "hanzo"):
                return "proj"
            elif (Hero == "mei") and (Hero == TempDPS[1]) and (TempDPS[0] == "hanzo"):
                return "proj"
            elif (Hero == "hanzo") and (Hero == TempDPS[0]) and (TempDPS[1] == "pharah"):
                return "hitscan"
            elif (Hero == "mei") and (Hero == TempDPS[0]) and (TempDPS[1] == "hanzo"):
                return "proj"
            elif (Hero == "mei") and (Hero == TempDPS[0]) and (TempDPS[1] == "doomfist"):
                return "hitscan"
            elif (Hero == "doomfist") and (Hero == TempDPS[1]) and (TempDPS[0] == "mei"):
                return "proj"
            elif (Hero == "mei") and (Hero == TempDPS[1]) and (TempDPS[0] == "doomfist"):
                return "hitscan"
            elif (Hero == "doomfist") and (Hero == TempDPS[0]) and (TempDPS[1] == "mei"):
                return "proj"
            elif (Hero == "bastion") and (Hero == TempDPS[0]) and (TempDPS[1] == "mei"):
                return "proj"
            elif (Hero == "sombra") and (Hero == TempDPS[0]) and (TempDPS[1] == "tracer"):
                return "hitscan"
            elif (Hero == "tracer") and (Hero == TempDPS[0]) and (TempDPS[1] == "sombra"):
                return "proj"
            elif (Hero == "sombra") and (Hero == TempDPS[1]) and (TempDPS[0] == "tracer"):
                return "hitscan"
            elif (Hero == "tracer") and (Hero == TempDPS[1]) and (TempDPS[0] == "sombra"):
                return "proj"
            elif (Hero == "hanzo") and (Hero == TempDPS[1]) and (TempDPS[0] == "bastion"):
                return "proj"
            elif (Hero == "hanzo") and (Hero == TempDPS[0]) and (TempDPS[1] == "bastion"):
                return "proj"
            elif (Hero == "mei") and (Hero == TempDPS[1]) and (TempDPS[0] == "bastion"):
                return "proj"
            elif (Hero == "mei") and (Hero == TempDPS[0]) and (TempDPS[1] == "bastion"):
                return "proj"
            elif (Hero == "sombra") and (Hero == TempDPS[1]) and (TempDPS[0] == "hanzo"):
                return "hitscan"
            elif (Hero == "sombra") and (Hero == TempDPS[0]) and (TempDPS[1] == "hanzo"):
                return "hitscan"
            elif (Hero == "hanzo") and (Hero == TempDPS[1]) and (TempDPS[0] == "sombra"):
                return "proj"
            elif (Hero == "hanzo") and (Hero == TempDPS[0]) and (TempDPS[1] == "sombra"):
                return "proj"
            elif (Hero == "torbjorn") and (Hero == TempDPS[1]) and (TempDPS[0] == "mei"):
                return "hitscan"
            elif (Hero == "torbjorn") and (Hero == TempDPS[0]) and (TempDPS[1] == "mei"):
                return "hitscan"
            elif (Hero == "mei") and (Hero == TempDPS[1]) and (TempDPS[0] == "torbjorn"):
                return "proj"
            elif (Hero == "mei") and (Hero == TempDPS[0]) and (TempDPS[1] == "torbjorn"):
                return "proj"
            elif (Hero == "doomfist") and (Hero == TempDPS[1]) and (TempDPS[0] == "sombra"):
                return "proj"
            elif (Hero == "doomfist") and (Hero == TempDPS[0]) and (TempDPS[1] == "sombra"):
                return "proj"
            elif (Hero == "sombra") and (Hero == TempDPS[1]) and (TempDPS[0] == "doomfist"):
                return "hitscan"
            elif (Hero == "sombra") and (Hero == TempDPS[0]) and (TempDPS[1] == "doomfist"):
                return "hitscan"
            elif (Hero == "mei") and (Hero == TempDPS[1]) and (TempDPS[0] == "symmetra"):
                return "proj"
            elif (Hero == "mei") and (Hero == TempDPS[0]) and (TempDPS[1] == "symmetra"):
                return "proj"
            elif (Hero == "symmetra") and (Hero == TempDPS[1]) and (TempDPS[0] == "mei"):
                return "hitscan"
            elif (Hero == "symmetra") and (Hero == TempDPS[0]) and (TempDPS[1] == "mei"):
                return "hitscan"
            elif (Hero == "doomfist") and (Hero == TempDPS[1]) and (TempDPS[0] == "hanzo"):
                return "proj"
            elif (Hero == "doomfist") and (Hero == TempDPS[0]) and (TempDPS[1] == "hanzo"):
                return "proj"
            elif (Hero == "hanzo") and (Hero == TempDPS[1]) and (TempDPS[0] == "doomfist"):
                return "hitscan"
            elif (Hero == "hanzo") and (Hero == TempDPS[0]) and (TempDPS[1] == "doomfist"):
                return "hitscan"
            elif (Hero == "mei") and (Hero == TempDPS[1]) and (TempDPS[0] == "sombra"):
                return "proj"
            elif (Hero == "mei") and (Hero == TempDPS[0]) and (TempDPS[1] == "sombra"):
                return "proj"
            elif (Hero == "sombra") and (Hero == TempDPS[1]) and (TempDPS[0] == "mei"):
                return "hitscan"
            elif (Hero == "sombra") and (Hero == TempDPS[0]) and (TempDPS[1] == "mei"):
                return "hitscan"
            elif (Hero == "tracer") and (Hero == TempDPS[1]) and (TempDPS[0] == "mei"):
                return "hitscan"
            elif (Hero == "tracer") and (Hero == TempDPS[0]) and (TempDPS[1] == "mei"):
                return "hitscan"
            elif (Hero == "mei") and (Hero == TempDPS[1]) and (TempDPS[0] == "tracer"):
                return "proj"
            elif (Hero == "mei") and (Hero == TempDPS[0]) and (TempDPS[1] == "tracer"):
                return "proj"
            elif (Hero == "tracer") and (Hero == TempDPS[1]) and (TempDPS[0] == "hanzo"):
                return "hitscan"
            elif (Hero == "tracer") and (Hero == TempDPS[0]) and (TempDPS[1] == "hanzo"):
                return "hitscan"
            elif (Hero == "hanzo") and (Hero == TempDPS[1]) and (TempDPS[0] == "tracer"):
                return "proj"
            elif (Hero == "hanzo") and (Hero == TempDPS[0]) and (TempDPS[1] == "tracer"):
                return "proj"
            elif (Hero == "tracer") and (Hero == TempDPS[1]) and (TempDPS[0] == "doomfist"):
                return "hitscan"
            elif (Hero == "tracer") and (Hero == TempDPS[0]) and (TempDPS[1] == "doomfist"):
                return "hitscan"
            elif (Hero == "doomfist") and (Hero == TempDPS[1]) and (TempDPS[0] == "tracer"):
                return "proj"
            elif (Hero == "doomfist") and (Hero == TempDPS[0]) and (TempDPS[1] == "tracer"):
                return "proj"
            elif (Hero == "bastion") and (Hero == TempDPS[0]) and (TempDPS[1] == "mei"):
                return "hitscan"
            elif (Hero == "bastion") and (Hero == TempDPS[1]) and (TempDPS[0] == "mei"):
                return "hitscan"
            elif (Hero == "mei") and (Hero == TempDPS[0]) and (TempDPS[1] == "bastion"):
                return "proj"
            elif (Hero == "mei") and (Hero == TempDPS[1]) and (TempDPS[0] == "bastion"):
                return "proj"
            elif (Hero in HitscanList):
                return "hitscan"
            elif (Hero in ProjList):
                return "proj"
            elif (Hero == TempDPS[0]) and (TempDPS[1] in ProjList):
                return "hitscan"
            elif (Hero == TempDPS[1]) and (TempDPS[0] in ProjList):
                return "hitscan"
            elif (Hero == TempDPS[0]) and (TempDPS[1] in HitscanList):
                return "proj"
            elif (Hero == TempDPS[1]) and (TempDPS[0] in HitscanList):
                return "proj"
        return "error"

    #Sort a list of ults by their execution time :eyes:
    def SortUltsByTime(self, Data):
        RangeLen = len(Data)

        for UltPos in range(RangeLen):

            for SortPos in range(0, RangeLen - UltPos - 1):
                if Data[SortPos]["time"] > Data[SortPos+1]["time"] :
                    Data[SortPos], Data[SortPos+1] = Data[SortPos+1], Data[SortPos]

        return Data

    #Clean the map and stage identifier
    def FindMap(self, Map):
        map   = ""
        stage = ""

        #TODO : Jesus please clean this, like fuck
        if "hanamura" in str(Map):
            map = "Hanamura"
        if "lunar" in str(Map):
            map = "Lunar"
        if "temple" in str(Map):
            map = "Temple of Anubis"
        if "volskaya" in str(Map):
            map = "Volskaya Industries"
        if "paris" in str(Map):
            map = "Paris"
        if "dorado" in str(Map):
            map = "Dorado"
        if "junkertown" in str(Map):
            map = "Junkertown"
        if "rialto" in str(Map):
            map = "Rialto"
        if "route" in str(Map):
            map = "Route 66"
        if "gibraltar" in str(Map):
            map = "Gibraltar"
        if "havana" in str(Map):
            map = "Havana"
        if "blizz" in str(Map):
            map = "Blizzard World"
        if "eichen" in str(Map):
            map = "Eichenwalde"
        if "hollywood" in str(Map):
            map = "Hollywood"
        if "kings" in str(Map):
            map = "King's Row"
        if "numbani" in str(Map):
            map = "Numbani"

        #Assigning the stage for KOTH
        if "lijiang" in str(Map):
            map = "Lijiang Tower"
            if "arket" in str(Map):
                stage = "Night Market"
            if "arden" in str(Map):
                stage = "Garden"
            if "ontrol" in str(Map):
                stage = "Control Center"
        if "oasis" in str(Map):
            map = "Oasis"
            if "ity" in str(Map):
                stage = "City Center"
            if "arden" in str(Map):
                stage = "Gardens"
            if "niversity" in str(Map):
                stage = "University"
        if "ilios" in str(Map):
            map = "Ilios"
            if "uin" in str(Map):
                stage = "Ruins"
            if "ell" in str(Map):
                stage = "Well"
            if "ight" in str(Map):
                stage = "Lighthouse"
        if "nepal" in str(Map):
            map = "Nepal"
            if "illage" in str(Map):
                stage = "Village"
            if "hrine" in str(Map):
                stage = "Shrine"
            if "anctum" in str(Map):
                stage = "Sanctum"
        if "busan" in str(Map):
            map = "Busan"
            if "own" in str(Map):
                stage = "Downtown"
            if "eka" in str(Map):
                stage = "MEKA base"
            if "anct" in str(Map):
                stage = "Sanctuary"


        return [map, stage]

    #Convert found data into csv
    def ConvertToCSV(self, Data):
        CsvOutput = ""
        for Rows in Data:
            for Columns in Rows:
                CsvOutput += str(Columns) + ", "

            CsvOutput += "\n"

        return CsvOutput



#Setup the App object containing the class
App = insightsGG.App()

#Create the cleaner
Cleaner = DataCleaner()


#Fetches teamfights
def FetchTeamFights():
    """
    TODO:
        - Clean this messy interface oh dear god
    """
    
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
    Title = [
        "Map",
        "Stage",
        " Start",
        " End",
        " Duration",
        " Winner",
        " BTank 1",
        " BTank 2",
        " BDps 1",
        " BDps 2",
        " BSupport 1",
        " BSupport 2",
        " RTank 1",
        " RTank 2",
        " RDps 1",
        " RDps 2",
        " RSupport 1",
        " RSupport 2",
        " BTank 1 Ult Usage",
        " BTank 2 Ult Usage",
        " BDps 1 Ult Usage",
        " BDps 2 Ult Usage",
        " BSupport 1 Ult Usage",
        " BSupport 2 Ult Usage",
        " RTank 1 Ult Usage",
        " RTank 2 Ult Usage",
        " RDps 1 Ult Usage",
        " RDps 2 Ult Usage",
        " RSupport 1 Ult Usage",
        " RSupport 2 Ult Usage",
        " Total Blue Ults",
        " Total Red Ults",
        " First Ult Team",
        " First Ult Caster",
        " First Kill Team",
        " First Kill Killer",
        " First Kill Killie",
        " Blue Kills",
        " Red Kills",
        " Blue MT Kills",
        " Blue MT Deaths",
        " Blue OT Kills",
        " Blue OT Deaths",
        " Blue HS Kills",
        " Blue HS Deaths",
        " Blue Proj Kills",
        " Blue Proj Deaths",
        " Blue FS Kills",
        " Blue FS Deaths",
        " Blue MS Kills",
        " Blue MS Deaths",
        " Red MT Kills",
        " Red MT Deaths",
        " Red OT Kills",
        " Red OT Deaths",
        " Red HS Kills",
        " Red HS Deaths",
        " Red Proj Kills",
        " Red Proj Deaths",
        " Red FS Kills",
        " Red FS Deaths",
        " Red MS Kills",
        " Red MS Deaths"
        ]
    Output = [Title]

    print("[LOG] Sorting matches...")

    #For each match analyzed
    for MatchUps in MatchAnalytics["matches"]:
        #For each fight in match
        for TeamFights in MatchUps["data"]["teamfights"]:
            #Setup the row output
            RowOutput = []

            #Setup heroes
            BLUEHEROES = []
            REDHEROES  = []

            roles      = ["maintank","offtank","hitscan", "proj","offsupport", "mainsupport"]
            BluTempSupp = []
            BluTempDPS = []
            BluTempTank = []
            RedTempSupp = []
            RedTempDPS = []
            RedTempTank = []

            BluMainTank = ""
            BluOffTank  = ""
            BluHitscan  = ""
            BluProj     = ""
            BluMainSupp = ""
            BluOffSupp  = ""

            RedMainTank = ""
            RedOffTank  = ""
            RedHitscan  = ""
            RedProj     = ""
            RedMainSupp = ""
            RedOffSupp  = ""

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
                if(Cleaner.FindRole(Hero) == "support"):
                    BluTempSupp.append(Hero)
                elif(Cleaner.FindRole(Hero) == "tank"):
                    BluTempTank.append(Hero)
                elif(Cleaner.FindRole(Hero) == "dps"):
                    BluTempDPS.append(Hero)

            for Hero in TeamFights["red_heroes"]:
                if(Cleaner.FindRole(Hero) == "support"):
                    RedTempSupp.append(Hero)
                elif(Cleaner.FindRole(Hero) == "tank"):
                    RedTempTank.append(Hero)
                elif(Cleaner.FindRole(Hero) == "dps"):
                    RedTempDPS.append(Hero)

            #Seperate Heros in each character type into roles
            for Role in roles:
                for Hero in BluTempSupp:
                    if(Cleaner.FindSecondaryRole(Hero, BluTempSupp, BluTempTank, BluTempDPS) == Role):
                        if Role == "mainsupport":
                            BluMainSupp = Hero
                        elif Role == "offsupport":
                            BluOffSupp = Hero
                for Hero in BluTempTank:
                    if(Cleaner.FindSecondaryRole(Hero, BluTempSupp, BluTempTank, BluTempDPS) == Role):
                        if Role == "maintank":
                            BluMainTank = Hero
                        elif Role == "offtank":
                            BluOffTank = Hero
                for Hero in BluTempDPS:
                    if(Cleaner.FindSecondaryRole(Hero, BluTempSupp, BluTempTank, BluTempDPS) == Role):
                        if Role == "hitscan":
                            BluHitscan = Hero
                        elif Role == "proj":
                            BluProj = Hero
                for Hero in RedTempSupp:
                    if(Cleaner.FindSecondaryRole(Hero, RedTempSupp, RedTempTank, RedTempDPS) == Role):
                        if Role == "mainsupport":
                            RedMainSupp = Hero
                        elif Role == "offsupport":
                            RedOffSupp = Hero
                for Hero in RedTempTank:
                    if(Cleaner.FindSecondaryRole(Hero, RedTempSupp, RedTempTank, RedTempDPS) == Role):
                        if Role == "maintank":
                            RedMainTank = Hero
                        elif Role == "offtank":
                            RedOffTank = Hero
                for Hero in RedTempDPS:
                    if(Cleaner.FindSecondaryRole(Hero, RedTempSupp, RedTempTank, RedTempDPS)== Role):
                        if Role == "hitscan":
                            RedHitscan = Hero
                        elif Role == "proj":
                            RedProj = Hero

            #Build team lists in role order
            BluTemp.append(BluMainTank)
            BluTemp.append(BluOffTank)
            BluTemp.append(BluHitscan)
            BluTemp.append(BluProj)
            BluTemp.append(BluOffSupp)
            BluTemp.append(BluMainSupp)

            RedTemp.append(RedMainTank)
            RedTemp.append(RedOffTank)
            RedTemp.append(RedHitscan)
            RedTemp.append(RedProj)
            RedTemp.append(RedOffSupp)
            RedTemp.append(RedMainSupp)

            #CSV Format Heroes - Sort through the Heroes, organize them for CSV, and flag which one ulted
            BlueUltBefore = []
            RedUltBefore  = []
            BlueUltAfter  = []
            RedUltAfter   = []

            #Comb through the ult usage | Blue team
            Counter = 0
            for Heroes in BluTemp:
                #Find if ult used
                if Heroes in BlueTempUltUsage:
                    BluUltUsage[Counter] = 1
                BLUEHEROES.append(Heroes)
                Counter += 1

                #Find the ult % before
                for Block in TeamFights["blue_team_ults_before"]:
                    if Block["hero"] == Heroes:
                        if Block["status"] == "ready":
                            Block["status"] = "100"
                        BlueUltBefore.append(str(Block["status"]))

                #Find the ult % afterwards
                for Block in TeamFights["blue_team_ults_after"]:
                    if Block["hero"] == Heroes:
                        if Block["status"] == "ready":
                            Block["status"] = "100"
                        BlueUltAfter.append(str(Block["status"]))

            #Comb through the ult usage | RED TEAM
            Counter = 0
            for Heroes in RedTemp:
                #Find if the ult was used
                if Heroes in RedTempUltUsage:
                    RedUltUsage[Counter] = 1
                REDHEROES.append(Heroes)
                Counter += 1

                #Find the ult % before
                for Block in TeamFights["red_team_ults_before"]:
                    if Block["hero"] == Heroes:
                        if Block["status"] == "ready":
                            Block["status"] = "100"
                        RedUltBefore.append(str(Block["status"]))

                #Find ult % afterwards
                for Block in TeamFights["red_team_ults_after"]:
                    if Block["hero"] == Heroes:
                        if Block["status"] == "ready":
                            Block["status"] = "100"
                        RedUltAfter.append(str(Block["status"]))

            #Total up the number
            TotalUltsBlu = sum(BluUltUsage)
            TotalUltsRed = sum(RedUltUsage)


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
            MapData = Cleaner.FindMap(MatchUps["data"]["map"])

            map = MapData[0]
            stage = MapData[1]


            #killcount
            BluMainTankKills = 0
            BluOffTankKills  = 0
            BluHitscanKills  = 0
            BluProjKills     = 0
            BluMainSuppKills = 0
            BluOffSuppKills  = 0

            RedMainTankKills = 0
            RedOffTankKills  = 0
            RedHitscanKills  = 0
            RedProjKills     = 0
            RedMainSuppKills = 0
            RedOffSuppKills  = 0

            #deathcount
            BluMainTankDeaths = 0
            BluOffTankDeaths  = 0
            BluHitscanDeaths  = 0
            BluProjDeaths     = 0
            BluMainSuppDeaths = 0
            BluOffSuppDeaths  = 0

            RedMainTankDeaths = 0
            RedOffTankDeaths  = 0
            RedHitscanDeaths  = 0
            RedProjDeaths     = 0
            RedMainSuppDeaths = 0
            RedOffSuppDeaths  = 0

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

            #Output
            RowOutput = [
        #Map Data
        map,
        stage,

        #Timing
        str(int(TeamFights["start_time"])),
        str(int(TeamFights["end_time"])),
        str(int(TeamFights["end_time"] - TeamFights["start_time"])),

        #Fight Winner
        TeamFights["winner"],

        #Blue team
        BLUEHEROES[0],
        BLUEHEROES[1],
        BLUEHEROES[2],
        BLUEHEROES[3],
        BLUEHEROES[4],
        BLUEHEROES[5],

        #Red team
        REDHEROES[0],
        REDHEROES[1],
        REDHEROES[2],
        REDHEROES[3],
        REDHEROES[4],
        REDHEROES[5],

        BluUltUsage[0],
        BluUltUsage[1],
        BluUltUsage[2],
        BluUltUsage[3],
        BluUltUsage[4],
        BluUltUsage[5],

        RedUltUsage[0],
        RedUltUsage[1],
        RedUltUsage[2],
        RedUltUsage[3],
        RedUltUsage[4],
        RedUltUsage[5],

        str(TotalUltsBlu),
        str(TotalUltsRed),

        FirstUltTeam,
        FirstUltTarget,
        FirstKillTeam,
        FirstKillKiller,
        FirstKillTarget,
        str(TeamFights["blue_team_kills"]),
        str(TeamFights["red_team_kills"]),
        str(BluMainTankKills),
        str(BluMainTankDeaths),
        str(BluOffTankKills),
        str(BluOffTankDeaths),
        str(BluHitscanKills),
        str(BluHitscanDeaths),
        str(BluProjKills),
        str(BluProjDeaths),
        str(BluMainSuppKills),
        str(BluMainSuppDeaths),
        str(BluOffSuppKills),
        str(BluOffSuppDeaths),
        str(RedMainTankKills),
        str(RedMainTankDeaths),
        str(RedOffTankKills),
        str(RedOffTankDeaths),
        str(RedHitscanKills),
        str(RedHitscanDeaths),
        str(RedProjKills),
        str(RedProjDeaths),
        str(RedMainSuppKills),
        str(RedMainSuppDeaths),
        str(RedOffSuppKills),
        str(RedOffSuppDeaths)
    ]
            Output.append(RowOutput)


    print("[LOG] Done sorting")

    #Convert output to CSV
    return Output


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
    FetchFights = FetchTeamFights()

    #Convert the output to CSV
    CsvOutput = Cleaner.ConvertToCSV(FetchFights)

    #Save output to CSV
    FileName = input("What would you like to save the file name as?: ")
    #Push the output
    with open("Outputs/" + FileName + ".csv", "w") as OutputFile:
        OutputFile.write(CsvOutput)



Start()
