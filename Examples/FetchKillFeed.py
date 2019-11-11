import insightsGG

import json

import sys


App = insightsGG.App()


def Login():
    #Check for cred
    Username = None
    Password = None

    #Check to see if user included login information in start (Uh this won't work if they have a space in their username or password, but I don't feel like fixing it...)
    if len(sys.argv) == 3:
        Username = sys.argv[1]
        Password = sys.argv[2]

    else:
        raise ValueError("[Error] Did not get a username and password to work with... Check the README and ensure you're following the instructions.")


    #We've got login data, login
    print("Got a username and password, logging in...")
    App.Login(Username, Password)
    print("Logged in...")





def Start():
    #Login
    Login()

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
    """
    #Write raw Analytics to a file
    with open("Outputs/Matches.json", "w") as File:
        json.dump(MatchAnalytics, File, sort_keys=True, indent=4)
        """


    #Create base csv
    CSVOutput = "Time, Killer Team, Killer, Target, Ability, Assist Tank, Assist Dps, Assist Heals,"

    #Loop through all of the kills
    for Matches in MatchAnalytics["matches"]:
        for KillBlocks in Matches["data"]["kills"]:

            #Setup Killer
            Killer      = KillBlocks["killer"]["hero"]
            KillerTeam  = KillBlocks["killer"]["color"]

            #Target
            Target      = KillBlocks["killee"]["hero"]

            #Ability used
            Ability     = ""

            if KillBlocks["ability"] == "none":
                Ability = " "
            elif KillBlocks["ability"] == None:
                Ability = " "

            else:
                Ability = KillBlocks["ability"]


            #Assists
            TankAssists    = []
            DPSAssists     = []
            SupportAssists = []

            #Loop through the assists, and organize them into role
            Assists = ""
            #Check and see if there are any assists
            if KillBlocks["assists"] is None:
                Assists = ""
            else:
                for Assists in KillBlocks["assists"]:
                    Role = FindRole(Assists)

                    if(Role == "tank"):
                        TankAssists.append(Assists + " ")

                    if(Role == "support"):
                        SupportAssists.append(Assists + " ")

                    if(Role == "dps"):
                        DPSAssists.append(Assists + " ")


            #Tanks
            if len(TankAssists) == 0:
                Assists += " "
            else:
                for Hero in TankAssists:
                    Assists += Hero + " "

            Assists += ","

            #DPS
            if len(DPSAssists) == 0:
                Assists += " "
            else:
                for Hero in DPSAssists:
                    Assists += Hero + " "

            Assists += ","

            #Supports
            if len(SupportAssists) == 0:
                Assists += " " + " "
            else:
                for Hero in SupportAssists:
                    Assists += Hero + " "

            #Test for suicide
            if KillerTeam == None:
                KillerTeam = KillBlocks["killee"]["color"]
            if Killer == None:
                Killer = KillBlocks["killee"]["hero"]


            #Add to output
            CSVOutput += "\n" + str(KillBlocks["start_time"]) + "," + KillerTeam + "," + Killer + "," + Target + "," + Ability + "," + Assists


    with open("Outputs/Test.csv", "w") as File:
        File.write(CSVOutput)


Start()
