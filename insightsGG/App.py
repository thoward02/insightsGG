#Imports
import json

from datetime import datetime

#Class imports
import insightsGG.Errors  as Errors
import insightsGG.Objects as Objects
import insightsGG.Objects.OverwatchAnalytics as OWAnalytics

from .Networking import NetworkManager

class App:
    #Data
    NetManager = NetworkManager()

    #User information
    Token       = None
    User        = None

    #Setup Teams
    Teams       = {}


    """
    ENTRY POINT
        == Contains ==
        Login(Username, Password) # For logging in
        BuildUser() #For constructing user infortmation during login

    """
    def Login(self, Username, Password):
        #Send the login request to the API
        LoginData = {
            "username" : Username,
            "password" : Password
        }

        LoginRequest = self.NetManager.SendLoginRequest(LoginData)

        #Check and see if login was right
        if "error" in LoginRequest:
            raise Errors.LoginError(LoginRequest["error"])

        #Pull Bearer token out of login request
        self.Token = LoginRequest["access_token"]

        #Grab user information, and store it in user
        self.User  = self.BuildUser()

        #Grab and store user's teams
        self.Teams = self.BuildTeams(100)

        #Done, send success
        return

    def BotLogin(self, Token):
        #Set token
        self.Token = Token

        #Check login
        Test = self.BuildUser()

        #IF login issue
        if Test == False:
            raise Errors.LoginError("INVALID TOKEN")

        #If login success
        self.User = Test

        #Go ahead and grab teams (assumably it's okay)
        self.Teams = self.BuildTeams(100)




    def BuildUser(self):
        #Return object
        UserInfo = {}

        #Build Request to fetch user info
        RequestData = {}

        RequestData["operationName"] = "GetUserProfileQuery"
        RequestData["variables"]     = {}
        RequestData["query"]         = self.NetManager.RequestOptions["GetUserProfileQuery"]

        RequestData                  = json.dumps(RequestData)

        #Send off the request
        UserInfo = self.NetManager.SendRequest(self.Token, RequestData)

        if UserInfo["data"] == None:
            return False

        #Ok so this is really weird, some times the api return the data in a `me` object and sometimes it doesn't
        if "me" in UserInfo["data"]:
            UserInfo = Objects.Me(UserInfo["data"]["me"])
        else:
            Userinfo = Objects.Me(UserInfo["data"])

        #return the info
        return UserInfo


    """
                              API FUNCTIONS
    ------------------------------------------------------------------------
    ========================= Team Functions ===============================
    ------------------------------------------------------------------------

    FetchTeams(TeamLimit)
        Grabs a `teamlimit` number of the teams user has access to

    GetTeamMembers(TeamId)
        Gets a list of members within the team

    GetInviteLinks(TeamId, InviteLinkLimit)
        Gets a list of active invite links

    GetPendingInvatations(TeamId)
        Gets a list of pending invites to a team
    ------------------------------------------------------------------------

    CreateTeam(TeamName, TeamDescription)
        Creates a team based on `TeamName` and `TeamDescription`

    DeleteTeam(TeamId)
        Deletes a team

    InviteToTeam(EmailList)
        Invites a list of players based on email addresses

    GenerateInviteLink(TeamId, Expire, Limit)
        Creates an invite link to a team. The expire can be

    DeleteInviteLink(TeamId, InviteId):
        Deletes an invite link

    RevokeInvatation(TeamId, InviteId)
        Revokes an invite to a player

    RemovePlayer(TeamId, PlayerId)
        Removes a player from a team

    ------------------------------------------------------------------------

    FetchRoles(TeamId)
        Fetches a list of roles on a team

    CreateRole(TeamId, Name, Colour, Privileges)
        Creates a role based on `Name` `Colour` and `Privileges`, where privileges
        are a list of strings that show what the user can acess,
        for example if you wanted a user to only access "Upload vods" and "Updating vods"
        privileges would equal ["UPDATE_VOD", "CREATE_VOD"]. Here's a full list of what privileges
        can hold:  ["CREATE_VOD", "UPDATE_VOD", "DELETE_VOD", "UPDATE_TAG",
        "CREATE_TAG", "DELETE_TAG", "ASSIGN_TAG", "DELETE_COMMENT", "UPDATE_COMMENT",
        "CREATE_COMMENT", "ASSIGN_ROLE", "UPDATE_ROLE", "DELETE_ROLE",
        "CREATE_ROLE", "REMOVE_MEMBER", "SEND_TEAM_INVITATION", "REVOKE_INVITATION", "UPDATE_TEAM", "START_SESSION"]

    DeleteRole(TeamId, RoleId)
        Deletes a role in a team

    AssignRoles(TeamId, PlayerId, Roles)
        Assigns a list of roles to a player, where in the `Roles` parameter
        contains a list of strings that contain the name of the roles you wish to assign
        for an example: ["Role1","Role2"]

    ------------------------------------------------------------------------
    ========================= VOD Functions ================================
    ------------------------------------------------------------------------

    GrabTeamVodList(TeamId, VodLimit)
        Grabs a `VodLimit` number of Vods that a particular team has

    ------------------------------------------------------------------------

    CreateVod(TeamId, VodLink)
        Creates a vod in a team, based off a link

    DeleteVod(VodId)
        Deletes a vod

    ModifyVod(VodId, Name, Public, OpenComments)
        Renames a vod, and sets it to be visable to the public as well as open
        to public comments

    RequestOverwatchAnalysis(VideoId)
        Requests an analysis on the video id

    ------------------------------------------------------------------------
    ========================= Tag Functions ================================
    ------------------------------------------------------------------------

    GetTags(TeamId, Limit)
        Gets all the tags on a team

    CreateTag(TeamId, Name, Colour)
        Creates a named tag and gives it an RGB colour

    DeleteTag(TeamId, TagId)
        Deletes a tag

    AddTags(VideoId, ListOfTagIds)
        Assigns a list of tags to a vod

    RemoveTags(VideoId, ListOfTagIds)
        Removes a list of tags from a vod

    ------------------------------------------------------------------------
    ========================= Stats Functions ==============================
    ------------------------------------------------------------------------

    GrabPrimaryRosterStats(Team)
        Grabs the list of players on your roster along with their stats

    GrabAnalytics(MatchId)
        Grabs the OverwatchAnalysis of a particular match

    ------------------------------------------------------------------------
    ======================= Owl Stats Functions ============================
    ------------------------------------------------------------------------
    GetOWLVideos(Year, Week, Limit)
        Grabs a list of the matches that happened on the Week of the Year. So
        if I wanted week one of 2020's vods, Year would be 2020 (int) and Week
        would be 1 (int). The amount of vods fetched is set by the limit
        function.

    ------------------------------------------------------------------------
    ======================= Core API functions =============================
    ------------------------------------------------------------------------
    CreateReturn(Success, Reason, Data):
        Creates a return back from the API Wrapper where Success is a bool
        indacating whether or whether not the call succeeded. Reason being
        a string containing the reason for an error, if an error has
        occurred, and Data being the data returned from a successful call.


    """

    """
    == TEAM FUNCTIONS ==
    """
    def FetchTeams(self, TeamLimit):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "GetTeamsQuery"
        RequestData["variables"]     = {"limit" : TeamLimit}
        RequestData["query"]         = self.NetManager.RequestOptions["GetTeamsQuery"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        TeamList = []

        #Loop through returned teams and store them
        for Teams in GrabRequest["data"]["queryTeams"]["teamEdges"]:
            TeamList.append(Objects.Team(self, Teams))

        return TeamList

    def GetTeamMembers(self, TeamId):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "GetMembersQuery"
        RequestData["variables"]     = {"teamId" : TeamId}
        RequestData["query"]         = self.NetManager.RequestOptions["GetMembersQuery"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest

    def GetInviteLinks(self, TeamId, InviteLinkLimit):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "GetInvitationsQuery"
        RequestData["variables"]     = {"teamId" : TeamId, "limit" : InviteLinkLimit}
        RequestData["query"]         = self.NetManager.RequestOptions["GetInvitationsQuery"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest

    def GetPendingInvatations(self, TeamId):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "GetPendingInvitationsQuery"
        RequestData["variables"]     = {"teamId" : TeamId}
        RequestData["query"]         = self.NetManager.RequestOptions["GetPendingInvitationsQuery"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest


    def CreateTeam(self, TeamName, TeamDescription):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "CreateTeamMutation"
        RequestData["variables"]     = {"input" : {"name" : TeamName, "description" : TeamDescription}}
        RequestData["query"]         = self.NetManager.RequestOptions["CreateTeamMutation"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up
        RequestFixed = GrabRequest["data"]["createTeam"]
        RequestFixed["roles"] = []

        #Clean up request, then store it
        return Objects.Team(self, RequestFixed)

    def EditTeamName(self, TeamId, Name):
        #Build Request Data
        RequestData = {}

        RequestData["operationName"] = "UpdateTeamMutation"
        RequestData["variables"]     = {"input" : {"teamId" : TeamId, "name" : Name}}
        RequestData["query"]         = self.NetManager.RequestOptions["UpdateTeamMutation"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest

    def DeleteTeam(self, TeamId):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "DeleteTeamMutation"
        RequestData["variables"]     = {"input" : {"id" : TeamId}}
        RequestData["query"]         = self.NetManager.RequestOptions["DeleteTeamMutation"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest


    def InviteToTeamEmail(self, TeamId, EmailList):
        #Build Email list
        EmailListObj = []
        for Emails in EmailList:
            EmailListObj.append({"email" : Emails})


        #Build Request
        RequestData = {}

        RequestData["operationName"] = "InviteMembersMutation"
        RequestData["variables"]     = {"input" : {"teamId" : TeamId, "invitations" : EmailListObj}}
        RequestData["query"]         = self.NetManager.RequestOptions["InviteMembersMutation"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest

    def CreateInviteLink(self, TeamId, Expire, Limit):
        #Format data
        Usage = None

        if Expire != None and Limit != None:
            if Expire > 5 or Expire < 1:
                raise ValueError("Expire should be either None type or have an int in the range of 1 - 5")

            ExpireTime = "P" + Expire + "D"
            Usage = {
                "teamId" : TeamId,
                "expiry" : ExpireTime,
                "limit"  : Limit
            }

        if Expire == None and Limit != None:
            Usage = {
                "teamId" : TeamId,
                "limit"  : Limit
            }

        if Expire != None and Limit == None:
            if Expire > 5 or Expire < 1:
                raise ValueError("Expire should be either None type or have an int in the range of 1 - 5")

            ExpireTime = "P" + Expire + "D"
            Usage = {
                "teamId" : TeamId,
                "expiry" : ExpireTime,
            }

        if Expire == None and Limit == None:
            Usage = {
                "teamId" : TeamId
            }

        #Build Request
        RequestData = {}

        RequestData["operationName"] = "CreateInvitationMutation"
        RequestData["variables"]     = {"input" : Usage}
        RequestData["query"]         = self.NetManager.RequestOptions["CreateInvitationMutation"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest

    def DeleteInviteLink(self, TeamId, InviteId):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "DeleteInvitationMutation"
        RequestData["variables"]     = {"input" : {"teamId" : TeamId, "invitationId" : InviteId}}
        RequestData["query"]         = self.NetManager.RequestOptions["DeleteInvitationMutation"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest

    def RevokeInvatation(self, TeamId, InvitationId):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "RevokeInvitationMutation"
        RequestData["variables"]     = {"input" : {"invitation" : {"teamId" : TeamId, "id" : InvitationId}}}
        RequestData["query"]         = self.NetManager.RequestOptions["RevokeInvitationMutation"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest

    def RemovePlayer(self, TeamId, PlayerId):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "RemoveMemberMutation"
        RequestData["variables"]     = {"input" : {"teamId" : TeamId, "memberId" : PlayerId}}
        RequestData["query"]         = self.NetManager.RequestOptions["RemoveMemberMutation"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest


    def FetchRoles(self, TeamId):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "GetRolesQuery"
        RequestData["variables"]     = {"teamId" : TeamId}
        RequestData["query"]         = self.NetManager.RequestOptions["GetRolesQuery"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest

    def CreateRole(self, TeamId, Name, Colour, Privileges):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "CreateRoleMutation"
        RequestData["variables"]     = {"input" : {"teamId" : TeamId, "name" : Name, "privileges" : Privileges, "color" : Colour}}
        RequestData["query"]         = self.NetManager.RequestOptions["CreateRoleMutation"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest

    def DeleteRole(self, TeamId, RoleId):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "DeleteRoleMutation"
        RequestData["variables"]     = {"input" : {"teamId" : TeamId, "id" : RoleId}}
        RequestData["query"]         = self.NetManager.RequestOptions["DeleteRoleMutation"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest

    def AssignRoles(self, TeamId, PlayerId, Roles):
        #Clean up roles
        TempRole = []
        for Role in Roles:
            TempRole.append({"name" : Role})

        Roles = TempRole

        #Build Request
        RequestData = {}

        RequestData["operationName"] = "AddMemberRolesMutation"
        RequestData["variables"]     = {"input" : {"teamId" : TeamId, "memberId" : PlayerId, "roles" : Roles}}
        RequestData["query"]         = self.NetManager.RequestOptions["AddMemberRolesMutation"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest


    """
    == VOD FUNCTIONS ==
    """
    def GrabTeamVodList(self, TeamId, VodLimit):
        RequestData = {}

        RequestData["operationName"] = "GetVideosQuery"
        RequestData["variables"]     = {
            "teamId" : TeamId,
            "limit"  : VodLimit
        }
        RequestData["query"]         = self.NetManager.RequestOptions["GetVideosQuery"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        VodList     = []

        for Vods in GrabRequest["data"]["queryVideos"]["videos"]:
            VodList.append(Objects.Video(ParentClass = self, InsightsObject = Vods))

        return VodList

    def CreateVod(self, TeamId, VodLink):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "CreateRemoteVideoMutation"
        RequestData["variables"]     = {"input" : {"remoteUrl" : VodLink, "teamId" : TeamId}}
        RequestData["query"]         = self.NetManager.RequestOptions["CreateRemoteVideoMutation"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest

    def DeleteVod(self, VodId):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "DeleteVideoMutation"
        RequestData["variables"]     = {"input" : {"id" : VodId}}
        RequestData["query"]         = self.NetManager.RequestOptions["DeleteVideoMutation"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest

    def ModifyVod(self, VideoId, Name, Public, OpenComments):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "UpdateVideoMutation"
        RequestData["variables"]     = {"input" : {"id" : VideoId, "name" : Name, "public" : Public, "openComments" : OpenComments}}
        RequestData["query"]         = self.NetManager.RequestOptions["UpdateVideoMutation"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest

    def RequestOverwatchAnalysis(self, VideoId):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "CreateAnalysisRequestMutation"
        RequestData["variables"]     = {"input" : {"type" : "OVERWATCH", "videoId" : VideoId}}
        RequestData["query"]         = self.NetManager.RequestOptions["CreateAnalysisRequestMutation"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest


    """
    == TAG FUNCTIONS ==
    """
    def GetTags(self, TeamId, Limit):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "GetTagsQuery"
        RequestData["variables"]     = {"teamId" : TeamId, "limit" : Limit}
        RequestData["query"]         = self.NetManager.RequestOptions["GetTagsQuery"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest["data"]["queryTags"]["tags"]

    def CreateTag(self, TeamId, Name, Colour):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "CreateTagMutation"
        RequestData["variables"]     = {"input" : {"teamId" : TeamId, "name" : Name, "color" : Colour}}
        RequestData["query"]         = self.NetManager.RequestOptions["CreateTagMutation"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest

    def DeleteTag(self, TeamId, TagId):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "DeleteTagMutation"
        RequestData["variables"]     = {"input" : {"teamId" : TeamId, "id" : TagId}}
        RequestData["query"]         = self.NetManager.RequestOptions["DeleteTagMutation"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest

    def AddTags(self, VideoId, ListOfTagIds):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "TagVideoMutation"
        RequestData["variables"]     = {"input" : {"videoId" : VideoId, "tagIds" : ListOfTagIds}}
        RequestData["query"]         = self.NetManager.RequestOptions["TagVideoMutation"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest

    def RemoveTags(self, VideoId, ListOfTagIds):
        #Build Request
        RequestData = {}

        RequestData["operationName"] = "UntagVideoMutation"
        RequestData["variables"]     = {"input" : {"videoId" : VideoId, "tagIds" : ListOfTagIds}}
        RequestData["query"]         = self.NetManager.RequestOptions["UntagVideoMutation"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        #Clean up request, then store it
        return GrabRequest


    """
    == STATS FUNCTIONS ==
    """
    def GrabPrimaryRosterStats(self, TeamId):
        RequestData = {}

        RequestData["operationName"] = "GetOverwatchPrimaryRosterPlayerStatisticsV2Query"
        RequestData["variables"]     = {
            "teamId" : TeamId
        }
        RequestData["query"]         = self.NetManager.RequestOptions["GetOverwatchPrimaryRosterPlayerStatisticsV2Query"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        return GrabRequest

    def GrabAnalytics(self, MatchIds):
        RequestData = {}

        RequestData["operationName"] = "GetMatchesByIdQuery"
        RequestData["variables"]     = {
            "ids" : MatchIds,
        }
        RequestData["query"]         = self.NetManager.RequestOptions["GetMatchesByIdQuery"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        ReturnList = []

        for Matches in GrabRequest["data"]["matches"]:
            ReturnList.append(OWAnalytics.Match(Matches))

        return ReturnList


    """
    == OWL STATS FUNCTIONS
    """
    def GetOWLVideos(self, Year, Week, Limit):
        RequestData = {}

        RequestData["operationName"] = "GetOWLVideosQuery"
        RequestData["variables"]     = {
            "year"  : Year,
            "week"  : Week,
            "limit" : Limit
        }
        RequestData["query"]         = self.NetManager.RequestOptions["GetOWLVideosQuery"]

        #Convert request to a string because GraphQL will only take a string request
        RequestData = json.dumps(RequestData)

        GrabRequest = self.NetManager.SendRequest(self.Token, RequestData)

        Timeline = GrabRequest["data"]

        return Timeline


    """
    == CORE API FUNCTIONS
    """
    def CreateReturn(self, Success, Reason, Data):
        RObj = {
            "Success" : Success,
            "Reason"  : Reason,
            "Data"    : Data
        }

        return RObj


    #Pretty prints
    def __str__(self):
        return json.dumps(self.toJSON(), indent=4,  separators=(',', ': '))

    #Creates custom json object representing object
    def toJSON(self):
        #Setup json vars
        TeamList = []

        for Teams in self.Teams:
            TeamList.append(Teams.Name)

        #Setup json object
        Object = {
            "User" : self.User.toJSON(), #I can't get this to pretty print as if we were in JS...,
            "Teams" : TeamList
        }

        #Return JSON object
        return Object


    ### DEPRECATED ###
    def BuildTeams(self, TeamLimit):
        return self.FetchTeams(TeamLimit)
