#Imports
import requests
import json

class App:
    #Login
    Username    = None
    Password    = None
    Token       = None

    #User information
    User        = None

    #Setup Teams
    Teams       = {}

    #Setup paths
    LoginPath   = "https://insights.gg/oauth/token"
    RequestPath = "https://insights.gg/graphql"

    #Setup the class constructor
    def __init__(self):
        with open("LibAssets/Requests.json") as RequestFile:
            self.RequestOptions = json.load(RequestFile)

    #Login Entry point
    def Login(self, Username, Password):
        #Setup username and password
        self.Username = Username
        self.Password = Password

        #Send the login request to the API
        LoginRequest = requests.post(url = self.LoginPath, data={"username":self.Username, "password" : self.Password})

        #Check and see if login was right
        Return = LoginRequest.json()

        if "error" in Return:
            raise ValueError("[Error] Username or password was incorrect")


        #Pull Bearer token out of login request
        self.Token = Return["access_token"]

        #Grab user information, and store it in user
        self.User  = self.BuildUser()

        #Grab and store user's teams
        self.Teams = self.BuildTeams(100)

        #Populate Teams with Vods
        for Teams in self.Teams:
            self.Teams[Teams]["VodList"] = self.GrabTeamVodList(self.Teams[Teams]["id"], 100)

    def BuildUser(self):
        #Return object
        UserInfo = {}

        #Build Request to fetch user info
        RequestData = {}

        RequestData["operationName"] = "GetUserProfileQuery"
        RequestData["variables"]     = {}
        RequestData["query"]          = self.RequestOptions["GetUserProfileQuery"]

        RequestData                  = json.dumps(RequestData)

        #Send off the request
        UserInfo = self.SendRequest(RequestData)

        #Ok so this is really weird, some times the api return the data in a `me` object and sometimes it doesn't
        if "me" in UserInfo["data"]:
            UserInfo = UserInfo["data"]["me"]
        else:
            Userinfo = UserInfo["data"]

        #return the info
        return UserInfo

    #Fetch all of the user's teams, return them in JSON object
    def BuildTeams(self, TeamLimit):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "GetTeamsQuery"
        RequestData["variables"]     = {"limit" : TeamLimit}
        RequestData["query"]         = self.RequestOptions["GetTeamsQuery"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.SendRequest(RequestData)

        #Clean up request, then store it
        TeamList = {}

        #Loop through returned teams and store them
        for Teams in GrabRequest["data"]["queryTeams"]["teamEdges"]:
            TeamName = Teams["team"]["name"]
            TeamList[TeamName] = {
                "id" : Teams["team"]["id"],
                "description" : Teams["team"]["description"],
                "owner" : Teams["team"]["owner"]["alias"]
            }

        return TeamList

    #Grab all of the VODs ina users team
    def GrabTeamVodList(self, TeamId, VodLimit):
        RequestData = {}

        RequestData["operationName"] = "GetVideosQuery"
        RequestData["variables"]     = {
            "teamId" : TeamId,
            "limit"  : VodLimit
        }
        RequestData["query"]         = self.RequestOptions["GetVideosQuery"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.SendRequest(RequestData)

        VodList     = {}

        for Vods in GrabRequest["data"]["queryVideos"]["videos"]:
            VodList[Vods["name"]] = Vods

        return VodList

    #Grab stats for your primary roster within a vod
    def GrabPrimaryRosterStats(self, TeamId, VideoId):
        RequestData = {}

        RequestData["operationName"] = "GetOverwatchPrimaryRosterPlayerStatisticsV2Query"
        RequestData["variables"]     = {
            "teamId" : TeamId,
            "videoId"  : [videoId]
        }
        RequestData["query"]         = self.RequestOptions["GetOverwatchPrimaryRosterPlayerStatisticsV2Query"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.SendRequest(RequestData)

        return GrabRequest

    def GrabAnalytics(self, MatchIds):
        RequestData = {}

        RequestData["operationName"] = "GetMatchesByIdQuery"
        RequestData["variables"]     = {
            "ids" : MatchIds,
        }
        RequestData["query"]         = self.RequestOptions["GetMatchesByIdQuery"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        Header = {"Authorization" : "Bearer " + self.Token, "content-type" : "application/json"}

        GrabRequest = requests.post(url = self.RequestPath, data=RequestData, headers=Header);

        Timeline = GrabRequest.json()["data"]

        return Timeline

    def SendRequest(self, Data):
        #Login header using user token grabbed in Login()
        Header = {"Authorization" : "Bearer " + self.Token, "content-type" : "application/json"}

        #Send the post request
        GrabRequest = requests.post(url = self.RequestPath, data=Data, headers=Header);

        #Return the raw json request
        return GrabRequest.json()
