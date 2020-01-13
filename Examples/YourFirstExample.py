"""
Here we're going to display what the insights API has to offer uwu
You'll need
    - The api installed (pip install insightsGG)
    - Your sanity c:
    - And a pro account for insights.gg
"""


#import the API Wrapper
import insightsGG


#Create the interface from which we will use the API Wrapper
App = insightsGG.App()

#Get the user's username and password to login
Username = input("What's your username for insights: ")
Password = input("What's your password for insights: ")

#Login to the app
LoginAttempt = App.Login(Username, Password)

if(LoginAttempt["Success"] == False ):
    print("Error! Unknown username or password!!")
    exit()

#Print out the list of teams
print("Here's your list of teams:")
print("-------------------------")
for Teams in App.Teams:
    print("\t" + Teams)


print("Done c:")
