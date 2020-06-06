#Import insights class
import insightsGG

#Import json for dealing with json
import json

#import math for mathmatical coolness (It's a math lib... like whaddya want me to say?)
import math

#import sys and os for python functions
import sys
import os

#Setup the App object containing the class
App = insightsGG.App()

#Converts data to CSV
def ConvertToCSV():
    #Find a heros' role based on their hero | TODO: Move this... It's really odd...
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
    CSVOutput = "Map ,Start, End, Duration, Winner, BTank 1, BTank 2, BDps 1, BDps 2, BSupport 1, BSupport 2, RTank 1, RTank 2, RDps 1, RDps 2, RSupport 1, RSupport 2, BTank 1 Before Ult %, BTank 2 Before Ult %, BDps 1 Before Ult %, BDps 2 Before Ult %, BSupport 1 Before Ult %, BSupport 2 Before Ult %, RTank 1 Before Ult %, RTank 2 Before Ult %, RDps 1 Before Ult %, RDps 2 Before Ult %, RSupport 1 Before Ult %, RSupport 2 Before Ult %, BTank 1 Ult Usage, BTank 2 Ult Usage, BDps 1 Ult Usage, BDps 2 Ult Usage, BSupport 1 Ult Usage, BSupport 2 Ult Usage, RTank 1 Ult Usage, RTank 2 Ult Usage, RDps 1 Ult Usage, RDps 2 Ult Usage, RSupport 1 Ult Usage, RSupport 2 Ult Usage, Total Blue Ults, Total Red Ults, BTank 1 After Ult %, BTank 2 After Ult %, BDps 1 After Ult %, BDps 2 After Ult %, BSupport 1 After Ult %, BSupport 2 After Ult %, RTank 1 After Ult %, RTank 2 After Ult %, RDps 1 After Ult %, RDps 2 After Ult %, RSupport 1 After Ult %, RSupport 2 After Ult %, First Ult Team, First Ult Caster, First Kill Team, First Kill Killer, First Kill Killie, Blue Kills, Red Kills,  "

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
            for Role in roles:
                for Hero in TeamFights["blue_heroes"]:
                    if(FindRole(Hero) == Role):
                        BluTemp.append(Hero)

                for Hero in TeamFights["red_heroes"]:
                    if(FindRole(Hero) == Role):
                        RedTemp.append(Hero)

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

            #Output - TODO, Clean this holy fuck it's messy dude
            CSVOutput += "\n" + str(MatchUps["data"]["map"]) + "," + str(TeamFights["start_time"]) + "," + str(TeamFights["end_time"]) + "," + str(TeamFights["end_time"] - TeamFights["start_time"]) + "," + TeamFights["winner"]  + "," + BLUEHEROES  + REDHEROES + BlueUltBefore + RedUltBefore + BlueUltsUsed +  RedUltsUsed + str(TotalUltsBlu) + "," + str(TotalUltsRed) + "," +  BlueUltAfter + RedUltAfter + FirstUltTeam + "," + FirstUltTarget + "," + FirstKillTeam + "," + FirstKillKiller + "," + FirstKillTarget + "," + str(TeamFights["blue_team_kills"]) + "," + str(TeamFights["red_team_kills"])

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
