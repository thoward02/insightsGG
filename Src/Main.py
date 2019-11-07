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


#Create instance and login
App = Insights.App(LoginData["username"], LoginData["password"])

print("Logging in... ")
App.Login()

print("Logged in, logging your teams")

for Teams in App.Teams:
    print(App.Teams[Teams])
