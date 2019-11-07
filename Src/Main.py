#import class
import Insights
import json

print("Welcome to the insights demo C:")

#Grab login data
try:
    with open("login.json") as LoginFile:
        LoginData = json.load(LoginFile)
except:
    print("Did you follow the Readme, and add your credentials to login.json?")
    raise ValueError("Check Login.json")

#Create instance and login
App = Insights.App(LoginData["username"], LoginData["password"])

print("Logging in... ")
App.Login()

print("Logged in, logging your teams\n************************************")

#Loop through each team
for Teams in App.Teams:
    print("\n[" + Teams + "]")
    print("    -- Vods --")

    #Loop through the team's vods
    for Vods in App.Teams[Teams]["VodList"]:
        #Check to see if the vod has been analyzed, say it has been
        VodAnalyzed = App.Teams[Teams]["VodList"][Vods]["latestAnalysis"]

        if(VodAnalyzed):
            print("        " + Vods + " | Analyzed")
        else:
            print("        " + Vods + " | Not Analyzed")
