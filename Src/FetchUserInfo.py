#Import the insights library
import Insights

#Import sys for argument catching
import sys

#Import os for file checking
import os

#For dealing with json
import json

#Setup the insights interface
App = Insights.App()

#Program entry point
def Start():
    #Check for cred
    Creds    = False
    Username = None
    Password = None

    #Check to see if user included login information in start (Uh this won't work if they have a space in their username or password, but I don't feel like fixing it...)
    if len(sys.argv) == 3:
        Creds    = True
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

    #We've got login data, login
    App.Login(Username, Password)


    #Fetch the user info
    UserInfo = App.User

    print(UserInfo)

    #Print it out
    print("You're on user:" + str(UserInfo["name"]))


#Entry point
Start()
