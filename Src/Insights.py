#Imports
import requests
import json

class App:
    #Login
    Username    = None
    Password    = None
    Token       = None

    Teams       = {}

    LoginPath   = "https://insights.gg/oauth/token"


    #Requests
    RequestPath = "https://insights.gg/graphql"

    #Setup the class constructor
    def __init__(self, Username, Password):
        self.Username = Username
        self.Password = Password

        with open("Requests.json") as RequestFile:
            self.RequestOptions = json.load(RequestFile)

    def Login(self):
        #Send login
        LoginRequest = requests.post(url = self.LoginPath, data={"username":self.Username, "password" : self.Password})

        #Pull Bearer token out of login request
        Return = LoginRequest.json()
        self.Token = Return["access_token"]

        #Grab and store user's teams
        self.Teams = self.GrabTeams(100)


    def GrabTeams(self, TeamLimit):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "GetTeamsQuery"
        RequestData["variables"]     = {"limit" : TeamLimit}
        RequestData["query"]         = self.RequestOptions["GetTeamsQuery"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        Header = {"Authorization" : "Bearer " + self.Token, "content-type" : "application/json"}

        GrabRequest = requests.post(url = self.RequestPath, data=RequestData, headers=Header);

        #Clean up request, then store it
        TeamList = {}

        #Loop through returned teams and store them
        for items in GrabRequest.json()["data"]["queryTeams"]["teamEdges"]:
            TeamName = items["team"]["name"]




    def MakeRequest(self, UserRequest):
        Header = {"Authorization" : "Bearer " + self.Token, "content-type" : "application/json"}

        Request = requests.post(url = self.RequestPath, data=UserRequest, headers=Header)
