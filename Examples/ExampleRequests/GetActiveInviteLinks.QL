{
  "operationName":"GetInvitationsQuery",
  "variables":{
    "teamId":"68ADJyplPEM1EwcV11gfGp",
    "limit":100
  },
  "query":"query GetInvitationsQuery($teamId: ID!, $limit: Int, $after: Cursor) {
      queryInvitations(teamId: $teamId, limit: $limit, after: $after) {
        invitations {
          ...Invitation2Fragment
          __typename
        }
        pageInfo {
          ...PageInfoFragment
          __typename
        }
        __typename
      }
    }

    fragment Invitation2Fragment on Invitation2 {
      id
      created
      team {
        ...TeamFragment
        __typename
      }
      code
      expiry
      limit
      roles
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

    fragment PageInfoFragment on QueryPageInfo {
      end
      more
      __typename
    }
    "
}
