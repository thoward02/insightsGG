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


x = App.GrabTimeLine(["2HyM0p0pgETw5QlTIJ3Ia"])

with open("Outputs/Output.json", "w") as OutputFile:
    OutputFile.write(json.dumps(x, indent=4))

print("done...")
