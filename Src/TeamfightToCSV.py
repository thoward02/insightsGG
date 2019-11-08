#import class
import Insights
import json
import math

App = Insights.App()

def Login():
    print(" -- Welcome to the Example CSV Report -- ")

    #Grab login data
    try:
        with open("login.json") as LoginFile:
            LoginData = json.load(LoginFile)
    except:
        print("[Error] Did you follow the Readme, and add your credentials to login.json?")
        raise ValueError("Check Login.json")

    #Create instance and login

    #Login
    print("[LOG] Logging in... ")
    App.Login(LoginData["username"], LoginData["password"])
    print("[LOG] Logged in. ")

def StartUserTask():
    #Define some base functions
    def FindRole(Hero):
        SupportList = ["lucio", "moira", "zenyatta", "brigitte", "mercy", "ana", "baptiste"]
        DPSList     = ["ashe", "bastion", "doomfist", "genji", "hanzo", "junkrat", "mccree","mei","pharah","reaper","soldier_76","sombra", "symmetra", "torbjorn", "tracer","widowmaker"]
        TankList    = ["dva","orisa","reinhardt", "roadhog", "winston", "wrecking_ball", "zarya", "sigma"]

        if(Hero in SupportList):
            return "support"
        if(Hero in DPSList):
            return "dps"
        if(Hero in TankList):
            return "tank"

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
    CSVOutput = "Start, End, Winner, BTank 1, BTank 2, BDps 1, BDps 2, BSupport 1, BSupport 2, RTank 1, RTank 2, RDps 1, RDps 2, RSupport 1, RSupport 2, BTank 1 Before Ult %, BTank 2 Before Ult %, BDps 1 Before Ult %, BDps 2 Before Ult %, BSupport 1 Before Ult %, BSupport 2 Before Ult %, RTank 1 Before Ult %, RTank 2 Before Ult %, RDps 1 Before Ult %, RDps 2 Before Ult %, RSupport 1 Before Ult %, RSupport 2 Before Ult %, Blue Ults Used, Red Ult Used, BTank 1 After Ult %, BTank 2 After Ult %, BDps 1 After Ult %, BDps 2 After Ult %, BSupport 1 After Ult %, BSupport 2 After Ult %, RTank 1 After Ult %, RTank 2 After Ult %, RDps 1 After Ult %, RDps 2 After Ult %, RSupport 1 After Ult %, RSupport 2 After Ult %, First Ult Team, First Ult Caster, First Kill Team, First Kill Killer, First Kill Killie, Blue Kills, Red Kills,  "

    print("[LOG] Sorting matches...")
    #For each match analyzed
    for MatchUps in MatchAnalytics["matches"]:
        #For each fight in match
        for TeamFights in MatchUps["data"]["teamfights"]:
            #Setup heroes
            BLUEHEROES = ""
            REDHEROES  = ""


            roles      = ["tank", "dps", "support"]
            BluTemp    = []
            RedTemp    = []

            #Easy organization of teams
            for Role in roles:
                for Hero in TeamFights["blue_heroes"]:
                    if(FindRole(Hero) == Role):
                        BluTemp.append(Hero)

                for Hero in TeamFights["red_heroes"]:
                    if(FindRole(Hero) == Role):
                        RedTemp.append(Hero)

            #CSV Format Heroes
            for Heroes in BluTemp:
                BLUEHEROES += Heroes + ", "

            for Heroes in RedTemp:
                REDHEROES += Heroes + ", "

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

            for Ults in TeamFights["blue_team_ults_used"]:
                BlueUltsUsed += Ults["hero"] + " "


            for Ults in TeamFights["red_team_ults_used"]:
                RedUltsUsed += Ults["hero"] + " "

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

            #Output - TODO, Clean this holy fuck it's messy dude
            CSVOutput += "\n" + str(TeamFights["start_time"]) + "," + str(TeamFights["end_time"]) + "," + TeamFights["winner"]  + "," + BLUEHEROES  + REDHEROES + BlueUltBefore + RedUltBefore + BlueUltsUsed + "," + RedUltsUsed + "," + BlueUltAfter + RedUltAfter + FirstUltTeam + "," + FirstUltTarget + "," + FirstKillTeam + "," + FirstKillKiller + "," + FirstKillTarget + "," + str(TeamFights["blue_team_kills"]) + "," + str(TeamFights["red_team_kills"])

    print("[LOG] Done sorting")

    FileName = input("What would you like to save the file name as?: ")
    #Push the output
    with open("Outputs/" + FileName + ".csv", "w") as OutputFile:
        OutputFile.write(CSVOutput)

    print("[LOG] Done! Exiting")



#Starting Point
Login()
StartUserTask()
