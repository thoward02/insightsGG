#import class
import Insights
import json

#Grab login data
with open("login.json") as LoginFile:
    LoginData = json.load(LoginFile)


#Create instance and login
App = Insights.App(LoginData["username"], LoginData["password"])
App.Login()

print(App.Teams)
