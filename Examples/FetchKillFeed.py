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


    #We've got login data, login
    print("Got a username and password, logging in...")
    App.Login(Username, Password)
    print("Logged in...")





def Start():
    #Login
    Login()

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
    CSVOutput = "Time, Killer Team, Killer, Target, Ability, Assist Hero 1, Assist Hero 2, Assist Hero 3, Assist Hero 4, Assist Hero 5, Assist Hero 6"

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

            #Loop through the assists, and organize them into role
            Assists = ""

            #If there are no assists, leave it blank
            if KillBlocks["assists"] is None:
                Assists = " , , , , , ,"

            #There are assists, loop through them and document them
            else:
                AssistCount = 0
                for AssistHero in KillBlocks["assists"]:
                  Assists += AssistHero + ","
                  AssistCount += 1

                #For all the missing heroes, fill in blank spots
                for MissingHeros in range(6 - AssistCount):
                  Assists += ", "


            #Test for suicide
            if KillerTeam == None:
                KillerTeam = KillBlocks["killee"]["color"]
            if Killer == None:
                Killer = KillBlocks["killee"]["hero"]


            #Add to output
            CSVOutput += "\n" + str(KillBlocks["start_time"]) + "," + KillerTeam + "," + Killer + "," + Target + "," + Ability + "," + Assists

    FileName = input("What file do you want to save it to?: ")

    with open("Outputs/" + FileName + ".csv", "w") as File:
        print("Saving to Outputs/" + FileName + ".csv")
        File.write(CSVOutput)

    print("Done...")

Start()
