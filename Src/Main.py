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

#Login
print("Logging in... ")
App.Login()
print("Logged in. ")

#Run user tasks
print("Running user tasks...")

#Loop in users team, grab list of vods, and grab analysis of vods
TeamName = "RedtailVods"
VodList = []
for Vods in App.Teams[TeamName]["VodList"]:
    print("[" + str(len(VodList)) + "]: " + Vods)
    VodList.append(Vods)

print("Which one do you wanna fetch the analysis for?")

Analyze = int(input("Vod Num: "))

RawMatchList = App.Teams[TeamName]["VodList"][VodList[Analyze]]["latestAnalysis"]["result"]["matches"]
IdList   = []

for Matches in RawMatchList:
    IdList.append(Matches["id"])

#Send of match id list to be read

TimeLine = App.GrabTimeLine(IdList)

with open("Outputs/Output.json", "w") as OutputFile:
    OutputFile.write(json.dumps(TimeLine, indent=4))


print("Done...")
