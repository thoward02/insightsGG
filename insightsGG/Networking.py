import requests
import json
from collections import namedtuple

class NetworkManager:
    #Setup paths
    LoginPath   = "https://insights.gg/oauth/token"
    RequestPath = "https://insights.gg/graphql"

    RequestOptions = {
        "GetUserProfileQuery" : "query GetUserProfileQuery {  me {    ...SelfFragment    __typename  }}fragment SelfFragment on Self {  id  name  email  alias  picture  verified  whitelisted  marketing  updates  __typename}",

        "GetTeamsQuery" : "query GetTeamsQuery($limit: Int, $after: Cursor) {queryTeams(limit: $limit, after: $after) {        teamEdges {          privileges          roles {            ...RoleFragment            __typename          }          team {            ...TeamFragment            __typename          }          __typename        }        pageInfo {          end          more          __typename        }        __typename      }    }        fragment RoleFragment on Role {      id      name      global      privileges      __typename    }        fragment TeamFragment on Team {      id      name      picture      description      owner {        __typename        ...ProfileFragment      }      activeSession      __typename    }        fragment ProfileFragment on Profile {      __typename      id      alias      picture    }    ",

        "GetMembersQuery" : "query GetMembersQuery($teamId: ID!, $limit: Int, $after: Cursor) {  queryMembers(teamId: $teamId, limit: $limit, after: $after) {    edges {      ...MemberFragment      added      __typename    }    pageInfo {      ...PageInfoFragment      __typename    }    __typename  }}fragment MemberFragment on Member {  id  added  nickname  roles {    id    __typename  }  privileges  user {    ...ProfileFragment    __typename  }  __typename}fragment ProfileFragment on Profile {  __typename  id  alias  picture}fragment PageInfoFragment on QueryPageInfo {  end  more  __typename}",

        "GetVideosQuery" : "query GetVideosQuery($teamId: ID, $limit: Int, $after: Cursor) {  queryVideos(teamId: $teamId, limit: $limit, after: $after) {    videos {      ...VideoFragment      __typename    }    pageInfo {      ...PageInfoFragment      __typename    }    __typename  }}fragment VideoFragment on Video {  id  created  filesize  name  streamUrl  remoteUrl  error  thumbnail  progress {    current    rate    total    __typename  }  uploaded  tags  duration  comments  public  owner {    ...OwnerFragment    __typename  }  userMetadata {    ...MetadataEntryFragment    __typename  }  latestAnalysis {    ...AnalysisFragment    __typename  }  __typename}fragment OwnerFragment on Owner {  __typename  ... on Self {    name    alias    email    picture    __typename  }  ... on Profile {    alias    picture    __typename  }  ... on Team {    id    name    picture    __typename  }}fragment MetadataEntryFragment on MetadataEntry {  name  value  __typename}fragment AnalysisFragment on Analysis {  id  type  created  completed  progress {    current    rate    total    __typename  }  result {    matches {      id      __typename    }    __typename  }  error  __typename}fragment PageInfoFragment on QueryPageInfo {  end  more  __typename}",

        "GetRolesQuery" : "query GetRolesQuery($teamId: ID!, $limit: Int, $after: Cursor) {    queryRoles(teamId: $teamId, limit: $limit, after: $after) {      roles {        ...RoleFragment        __typename      }      pageInfo {        ...PageInfoFragment        __typename      }      __typename    }  }  fragment RoleFragment on Role {    id    name    global    privileges    color    __typename  }  fragment PageInfoFragment on QueryPageInfo {    end    more    __typename  }  ",

        "CreateRoleMutation" : "mutation CreateRoleMutation($input: CreateRoleInput!) {    createRole(input: $input) {      role {        ...RoleFragment        __typename      }      __typename    }  }  fragment RoleFragment on Role {    id    name    global    privileges    color    __typename  }  ",

        "DeleteRoleMutation" : "mutation DeleteRoleMutation($input: DeleteRole2Input!) {    deleteRole2(input: $input) {      id      __typename    }  }  ",

        "AddMemberRolesMutation" : "mutation AddMemberRolesMutation($input: AddMemberRolesInput!) {    addMemberRoles(input: $input) {      member {        ...MemberFragment        __typename      }      __typename    }  }  fragment MemberFragment on Member {    id    added    nickname    roles {      id      __typename    }    privileges    user {      ...ProfileFragment      __typename    }    __typename  }  fragment ProfileFragment on Profile {    __typename    id    alias    picture  }  ",

        "GetOverwatchPrimaryRosterPlayerStatisticsV2Query" : "query GetOverwatchPrimaryRosterPlayerStatisticsV2Query($teamId: ID, $videoIds: [ID!]) {  statistics(teamId: $teamId, type: OVERWATCH, videoIds: $videoIds) {    ... on OverwatchStatistics {      __typename      primaryRosterV2 {        name        players {          ...OverwatchPlayerStatisticsV2Fragment          __typename        }        __typename      }    }    __typename  }}fragment OverwatchPlayerStatisticsV2Fragment on OverwatchPlayerStatisticsV2 {  playerId  playerName  kills  deaths  ults  time  firstDeaths  firstKills  firstUlts  assists  heroes {    ...OverwatchPlayerHeroStatisticsFragment    __typename  }  __typename}fragment OverwatchPlayerHeroStatisticsFragment on OverwatchPlayerHeroStatistics {  name  teamfights  firstKills  firstDeaths  ults  firstUlts  totalChargeTime  numUltCharge  totalHoldTime  time  kills  deaths  assists  __typename}",

        "GetMatchesByIdQuery" : "query GetMatchesByIdQuery($ids: [ID!]!) {  matches(ids: $ids) {    ...MatchFragment    __typename  }}fragment MatchFragment on Match {  __typename  id  created  owner {    ...OwnerFragment    __typename  }  name  userMetadata {    name    value    __typename  }  ... on UserMatch {    video {      id      __typename    }    startTime    endTime    __typename  }  ... on GeneratedOverwatchMatch {    gvideo: video {      id      __typename    }    analysis {      id      __typename    }    gstartTime: startTime    gendTime: endTime    data    __typename  }}fragment OwnerFragment on Owner {  __typename  ... on Self {    name    alias    email    picture    __typename  }  ... on Profile {    alias    picture    __typename  }  ... on Team {    id    name    picture    __typename  }}",

        "CreateTeamMutation" : "mutation CreateTeamMutation($input: CreateTeamInput!) {  createTeam(input: $input) {    team {      ...TeamFragment          }      }}fragment TeamFragment on Team {  id  name  picture  description  owner {        ...ProfileFragment  }  activeSession  }fragment ProfileFragment on Profile {    id  alias  picture}",

        "UpdateTeamMutation" : "mutation UpdateTeamMutation($input: UpdateTeamInput!) {  updateTeam(input: $input) {    team {      ...TeamFragment      __typename    }    __typename  }}fragment TeamFragment on Team {  id  name  picture  description  owner {    __typename    ...ProfileFragment  }  activeSession  __typename}fragment ProfileFragment on Profile {  __typename  id  alias  picture}",

        "DeleteTeamMutation" : "mutation DeleteTeamMutation($input: DeleteTeamInput!) {  deleteTeam(input: $input) {    teamId    __typename  }}",

        "InviteMembersMutation" : "mutation InviteMembersMutation($input: InviteMembersInput!) {  inviteMembers(input: $input) {    invitations {      ...CreatedInvitationPayloadFragment      __typename    }    __typename  }}fragment CreatedInvitationPayloadFragment on CreatedInvitationPayload {  invitation {    ...InvitationFragment    __typename  }  code  __typename}fragment InvitationFragment on Invitation {  id  expiry  to  created  from {    ...ProfileFragment    __typename  }  target {    ...InvitationTargetFragment    __typename  }  __typename}fragment ProfileFragment on Profile {  __typename  id  alias  picture}fragment InvitationTargetFragment on InvitationTarget {  __typename  ... on Team {    id    name    __typename  }  ... on Video {    id    name    __typename  }}",

        "CreateInvitationMutation" : "mutation CreateInvitationMutation($input: CreateInvitationInput!) {    createInvitation(input: $input) {      invitation {        ...Invitation2Fragment        __typename      }      __typename    }  }  fragment Invitation2Fragment on Invitation2 {    id    created    team {      ...TeamFragment      __typename    }    code    expiry    limit    roles    privileges    __typename  }  fragment TeamFragment on Team {    id    name    picture    description    owner {      __typename      ...ProfileFragment    }    activeSession    __typename  }  fragment ProfileFragment on Profile {    __typename    id    alias    picture  }  ",

        "GetInvitationsQuery" : "query GetInvitationsQuery($teamId: ID!, $limit: Int, $after: Cursor) {    queryInvitations(teamId: $teamId, limit: $limit, after: $after) {      invitations {        ...Invitation2Fragment        __typename      }      pageInfo {        ...PageInfoFragment        __typename      }      __typename    }  }  fragment Invitation2Fragment on Invitation2 {    id    created    team {      ...TeamFragment      __typename    }    code    expiry    limit    roles    privileges    __typename  }  fragment TeamFragment on Team {    id    name    picture    description    owner {      __typename      ...ProfileFragment    }    activeSession    __typename  }  fragment ProfileFragment on Profile {    __typename    id    alias    picture  }  fragment PageInfoFragment on QueryPageInfo {    end    more    __typename  }  ",

        "GetPendingInvitationsQuery" : "query GetPendingInvitationsQuery($teamId: ID, $videoId: ID, $limit: Int, $after: Cursor) {    queryPendingInvitations(teamId: $teamId, videoId: $videoId, limit: $limit, after: $after) {      invitations {        ...InvitationFragment        __typename      }      pageInfo {        ...PageInfoFragment        __typename      }      __typename    }  }  fragment InvitationFragment on Invitation {    id    expiry    to    created    from {      ...ProfileFragment      __typename    }    target {      ...InvitationTargetFragment      __typename    }    __typename  }  fragment ProfileFragment on Profile {    __typename    id    alias    picture  }  fragment InvitationTargetFragment on InvitationTarget {    __typename    ... on Team {      id      name      __typename    }    ... on Video {      id      name      __typename    }  }  fragment PageInfoFragment on QueryPageInfo {    end    more    __typename  }",

        "DeleteInvitationMutation" : "mutation DeleteInvitationMutation($input: DeleteInvitationInput!) {  deleteInvitation(input: $input) {    id    __typename  }}",

        "RevokeInvitationMutation" : "mutation RevokeInvitationMutation($input: RevokeInvitationInput!) {    revokeInvitation(input: $input) {      invitationId      __typename    }  }  ",

        "RemoveMemberMutation" : "mutation RemoveMemberMutation($input: RemoveMemberInput!) {    removeMember(input: $input) {      memberId      __typename    }  }  ",

        "CreateRemoteVideoMutation" : "mutation CreateRemoteVideoMutation($input: CreateRemoteVideoInput!) {  createRemoteVideo(input: $input) {    video {      ...VideoFragment    }  }}fragment VideoFragment on Video {  id  created  filesize  name  streamUrl  remoteUrl  error  thumbnail  progress {    current    rate    total  }  uploaded  tags  duration  comments  public  owner {    ...OwnerFragment  }  userMetadata {    ...MetadataEntryFragment  }  latestAnalysis {    ...AnalysisFragment  }}fragment OwnerFragment on Owner {  ... on Self {    name    alias    email    picture  }  ... on Profile {    alias    picture  }  ... on Team {    id    name    picture  }}fragment MetadataEntryFragment on MetadataEntry {  name  value}fragment AnalysisFragment on Analysis {  id  type  created  completed  progress {    current    rate    total  }  result {    matches {      id    }  }  error}",

        "UpdateVideoMutation" : "mutation UpdateVideoMutation($input: UpdateVideoInput!) {  updateVideo(input: $input) {    video {      ...VideoFragment      __typename    }    __typename  }}fragment VideoFragment on Video {  id  created  filesize  name  streamUrl  remoteUrl  error  thumbnail  progress {    current    rate    total    __typename  }  uploaded  tags  duration  comments  public  openComments  owner {    ...OwnerFragment    __typename  }  userMetadata {    ...MetadataEntryFragment    __typename  }  latestAnalysis {    ...AnalysisFragment    __typename  }  __typename}fragment OwnerFragment on Owner {  __typename  ... on Self {    name    alias    email    picture    __typename  }  ... on Profile {    alias    picture    __typename  }  ... on Team {    id    name    picture    __typename  }}fragment MetadataEntryFragment on MetadataEntry {  name  value  __typename}fragment AnalysisFragment on Analysis {  id  type  created  completed  progress {    current    rate    total    __typename  }  result {    matches {      id      __typename    }    __typename  }  error  __typename}",

        "DeleteVideoMutation" : "mutation DeleteVideoMutation($input: DeleteVideoInput!) {    deleteVideo(input: $input) {      videoId      __typename    }  }",

        "CreateAnalysisRequestMutation" : "mutation CreateAnalysisRequestMutation($input: CreateAnalysisRequestInput!) {    createAnalysisRequest(input: $input) {      analysis {        ...AnalysisFragment        __typename      }      __typename    }  }  fragment AnalysisFragment on Analysis {    id    type    created    completed    progress {      current      rate      total      __typename    }    result {      matches {        id        __typename      }      __typename    }    error    __typename  }  ",

        "GetTagsQuery" : "query GetTagsQuery($teamId: ID, $limit: Int, $after: Cursor){ queryTags(teamId: $teamId, limit: $limit, after: $after){        tags {  id    name    color    __typename  }   pageInfo {     end    more      }    }}",

        "CreateTagMutation" : "mutation CreateTagMutation($input: CreateTagInput!) {    createTag(input: $input) {      tag {        ...TagFragment        __typename      }      __typename    }  }  fragment TagFragment on Tag {    id    name    color    __typename  }  ",

        "DeleteTagMutation" : "mutation DeleteTagMutation($input: DeleteTagInput!) {  deleteTag(input: $input) {    tagId    __typename  }}",

        "TagVideoMutation" : "mutation TagVideoMutation($input: TagVideoInput!) {    tagVideo(input: $input) {      video {        id        tags        __typename      }      __typename    }  }  ",

        "UntagVideoMutation" : "mutation UntagVideoMutation($input: UntagVideoInput!) {    untagVideo(input: $input) {      video {        id        tags        __typename      }      __typename    }  }  ",

        #OWL Stuff
        "GetOWLVideosQuery" : "query GetOWLVideosQuery($week: Int!, $year: Int!, $limit: Int, $after: Cursor) {  queryOWLVideos(week: $week, year: $year, limit: $limit, after: $after) {    videos {      ...VideoFragment      latestAnalysis {        result {          matches {            ...MatchFragment            __typename          }          __typename        }        __typename      }      __typename    }    pageInfo {      ...PageInfoFragment      __typename    }    __typename  }}fragment VideoFragment on Video {  id  created  filesize  name  streamUrl  remoteUrl  error  thumbnail  latestAnalysis {    ...AnalysisFragment    __typename  }  __typename}fragment AnalysisFragment on Analysis {  id  type  created  completed  progress {    current    rate    total    __typename  }  result {    matches {      id      __typename    }    __typename  }  error  __typename}fragment PageInfoFragment on QueryPageInfo {  end  more  __typename}fragment MatchFragment on Match {  __typename  id  created  name  ... on GeneratedMatch {    video {      id      __typename    }    analysis {      id      __typename    }    startTime    endTime    __typename  }  ... on GeneratedOverwatchMatch {    owdata: data    __typename  } }"


    }


    #Send login request using uname and pword
    def SendLoginRequest(self, LoginData):
        LoginRequest = requests.post(url = self.LoginPath, data = LoginData)

        #Return the raw json request
        return LoginRequest.json()

    #Send generic request
    def SendRequest(self, Token, Data):
        #Login header using user token grabbed in Login()
        Header = {"Authorization" : "Bearer " + Token, "content-type" : "application/json"}

        #Send the post request
        GrabRequest = requests.post(url = self.RequestPath, data=Data, headers=Header);

        #Return the raw json request
        return GrabRequest.json()
