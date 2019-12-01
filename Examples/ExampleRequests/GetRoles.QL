{
  "operationName":"GetRolesQuery",
  "variables":{
    "teamId":"68ADJyplPEM1EwcV11gfGp"
  },
  "query":"query GetRolesQuery($teamId: ID!, $limit: Int, $after: Cursor) {
      queryRoles(teamId: $teamId, limit: $limit, after: $after) {
        roles {
          ...RoleFragment
          __typename
        }
        pageInfo {
          ...PageInfoFragment
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
      color
      __typename
    }

    fragment PageInfoFragment on QueryPageInfo {
      end
      more
      __typename
    }
    "
}
