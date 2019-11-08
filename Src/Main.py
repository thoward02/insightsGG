#import class
import Insights
import json

App = Insights.App()

def Login():
    print("Welcome to the example CSV report")

    #Grab login data
    try:
        with open("login.json") as LoginFile:
            LoginData = json.load(LoginFile)
    except:
        print("Did you follow the Readme, and add your credentials to login.json?")
        raise ValueError("Check Login.json")

    #Create instance and login

    #Login
    print("Logging in... ")
    App.Login(LoginData["username"], LoginData["password"])
    print("Logged in. ")

def StartUserTask():
    #Define some base functions
    def FindRole(Hero):
        SupportList = ["lucio", "moira", "zenyatta", "brigitte", "mercy", "ana", "baptiste"]
        DPSList     = ["ashe", "bastion", "doomfist", "genji", "hanzo", "junkrat", "mccree","mei","pharah","reaper","soldier_76","sombra", "symmetra", "torbjorn", "tracer","widowmaker"]
        TankList    = ["dva","orisa","reinhardt", "roadhog", "winston", "wrecking_ball", "zarya"]

        if(Hero in SupportList):
            return "support"
        if(Hero in DPSList):
            return "dps"
        if(Hero in TankList):
            return "tank"

        return "error"

    #Loop in users team, grab list of vods, and grab analysis of vods
    TeamName = "RedtailVods"
    #TeamName = input("What Team do you want to index?: ")

    #Fetch vods
    VodList = []
    for Vods in App.Teams[TeamName]["VodList"]:
        print("[" + str(len(VodList)) + "]: " + Vods)
        VodList.append(Vods)

    #Ask user what vod they want
    print("Which one do you wanna fetch the analysis for?")

    Analyze = int(input("Vod Num: "))

    #Fetch the analysis for that vod
    RawMatchList = App.Teams[TeamName]["VodList"][VodList[Analyze]]["latestAnalysis"]["result"]["matches"]
    IdList   = []

    for Matches in RawMatchList:
        IdList.append(Matches["id"])


    #Send of match id list to be read
    MatchAnalytics = App.GrabAnalytics(IdList)

    #Create a custom CSV based on what we want
    CSVOutput = "Start, End, Winner, Blue Comp, Red Comp, Blue Ult % Before, Red Ult % Before, Blue Ults Used, Red Ult Used, Blue Ult % After, Red Ult % After, First Ult, First Kill, First Death, Blue Kills, Red Kills,  "

    print("Sorting matches...")
    for MatchUps in MatchAnalytics["matches"]:
        for TeamFights in MatchUps["data"]["teamfights"]:
            #Clean Heroes first

            #Fetch Heroes
            BLUEHEROES    = ""
            for Heroes in TeamFights["blue_heroes"]:
                BLUEHEROES += Heroes + " "


            REDHEROES     = ""
            for Heroes in TeamFights["blue_heroes"]:
                REDHEROES += Heroes + " "

            #Fetch Ults
            BlueUltBefore = ""
            for Ults in TeamFights["blue_team_ults_before"]:
                if(Ults["status"] == "ready"):
                    Ults["status"] = "100"
                BlueUltBefore += Ults["hero"] + "_" + str(Ults["status"]) + "% "


            RedUltBefore  = ""
            for Ults in TeamFights["red_team_ults_before"]:
                RedUltBefore += Ults["hero"] + "%" + str(Ults["status"]) + " "


            BlueUltAfter = ""
            for Ults in TeamFights["blue_team_ults_after"]:
                BlueUltAfter += Ults["hero"] + "%" + str(Ults["status"]) + " "


            RedUltAfter  = ""
            for Ults in TeamFights["red_team_ults_after"]:
                RedUltAfter += Ults["hero"] + "%" + str(Ults["status"]) + " "


            #Output
            CSVOutput += "\n" + str(TeamFights["start_time"]) + "," + str(TeamFights["end_time"])  + "," + TeamFights["winner"]  + "," + BLUEHEROES  + "," + REDHEROES + "," + BlueUltBefore + "," + RedUltBefore + "," + "NULL" + "," + "NULL" + "," + BlueUltAfter + "," + RedUltAfter + ", NULL, NULL, NULL, NULL, NULL"

    print("Done sorting")

    print("Writing CSV...")
    #Push the output
    with open("Outputs/Test.csv", "w") as OutputFile:
        OutputFile.write(CSVOutput)

    print("Done")



#Starting Point
Login()
StartUserTask()
