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

    RequestOptions = {
      "GetUserProfileQuery" : "query GetUserProfileQuery {  me {    ...SelfFragment    __typename  }}fragment SelfFragment on Self {  id  name  email  alias  picture  verified  whitelisted  marketing  updates  __typename}",

       "GetTeamsQuery" : "query GetTeamsQuery($limit: Int, $after: Cursor) {queryTeams(limit: $limit, after: $after) {        teamEdges {          privileges          roles {            ...RoleFragment            __typename          }          team {            ...TeamFragment            __typename          }          __typename        }        pageInfo {          end          more          __typename        }        __typename      }    }        fragment RoleFragment on Role {      id      name      global      privileges      __typename    }        fragment TeamFragment on Team {      id      name      picture      description      owner {        __typename        ...ProfileFragment      }      activeSession      __typename    }        fragment ProfileFragment on Profile {      __typename      id      alias      picture    }    ",

       "GetVideosQuery" : "query GetVideosQuery($teamId: ID, $limit: Int, $after: Cursor) {  queryVideos(teamId: $teamId, limit: $limit, after: $after) {    videos {      ...VideoFragment      __typename    }    pageInfo {      ...PageInfoFragment      __typename    }    __typename  }}fragment VideoFragment on Video {  id  created  filesize  name  streamUrl  remoteUrl  error  thumbnail  progress {    current    rate    total    __typename  }  uploaded  tags  duration  comments  public  owner {    ...OwnerFragment    __typename  }  userMetadata {    ...MetadataEntryFragment    __typename  }  latestAnalysis {    ...AnalysisFragment    __typename  }  __typename}fragment OwnerFragment on Owner {  __typename  ... on Self {    name    alias    email    picture    __typename  }  ... on Profile {    alias    picture    __typename  }  ... on Team {    id    name    picture    __typename  }}fragment MetadataEntryFragment on MetadataEntry {  name  value  __typename}fragment AnalysisFragment on Analysis {  id  type  created  completed  progress {    current    rate    total    __typename  }  result {    matches {      id      __typename    }    __typename  }  error  __typename}fragment PageInfoFragment on QueryPageInfo {  end  more  __typename}",

       "GetOverwatchPrimaryRosterPlayerStatisticsV2Query" : "query GetOverwatchPrimaryRosterPlayerStatisticsV2Query($teamId: ID, $videoIds: [ID!]) {  statistics(teamId: $teamId, type: OVERWATCH, videoIds: $videoIds) {    ... on OverwatchStatistics {      __typename      primaryRosterV2 {        name        players {          ...OverwatchPlayerStatisticsV2Fragment          __typename        }        __typename      }    }    __typename  }}fragment OverwatchPlayerStatisticsV2Fragment on OverwatchPlayerStatisticsV2 {  playerId  playerName  kills  deaths  ults  time  firstDeaths  firstKills  firstUlts  assists  heroes {    ...OverwatchPlayerHeroStatisticsFragment    __typename  }  __typename}fragment OverwatchPlayerHeroStatisticsFragment on OverwatchPlayerHeroStatistics {  name  teamfights  firstKills  firstDeaths  ults  firstUlts  totalChargeTime  numUltCharge  totalHoldTime  time  kills  deaths  assists  __typename}",

       "GetMatchesByIdQuery" : "query GetMatchesByIdQuery($ids: [ID!]!) {  matches(ids: $ids) {    ...MatchFragment    __typename  }}fragment MatchFragment on Match {  __typename  id  created  owner {    ...OwnerFragment    __typename  }  name  userMetadata {    name    value    __typename  }  ... on UserMatch {    video {      id      __typename    }    startTime    endTime    __typename  }  ... on GeneratedOverwatchMatch {    gvideo: video {      id      __typename    }    analysis {      id      __typename    }    gstartTime: startTime    gendTime: endTime    data    __typename  }}fragment OwnerFragment on Owner {  __typename  ... on Self {    name    alias    email    picture    __typename  }  ... on Profile {    alias    picture    __typename  }  ... on Team {    id    name    picture    __typename  }}"

    }

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
