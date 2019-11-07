[
{
"operationName" : "GetTeamsQuery",
"variables":{"limit":100},
"query" : "query GetTeamsQuery($limit: Int, $after: Cursor) {
  queryTeams(limit: $limit, after: $after) {
    teamEdges {
      privileges
      roles {
        ...RoleFragment
        __typename
      }
      team {
        ...TeamFragment
        __typename
      }
      __typename
    }
    pageInfo {
      end
      more
      __typename
    }
    __typename
  }
}

fragment RoleFragment on Role {
  id
  name
  global
  privileges
  __typename
}

fragment TeamFragment on Team {
  id
  name
  picture
  description
  owner {
    __typename
    ...ProfileFragment
  }
  activeSession
  __typename
}

fragment ProfileFragment on Profile {
  __typename
  id
  alias
  picture
}
"}]
