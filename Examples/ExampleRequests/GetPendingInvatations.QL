{
  "operationName":"GetPendingInvitationsQuery",
  "variables":{
    "teamId":"68ADJyplPEM1EwcV11gfGp"
  },
  "query":"query GetPendingInvitationsQuery($teamId: ID, $videoId: ID, $limit: Int, $after: Cursor) {
      queryPendingInvitations(teamId: $teamId, videoId: $videoId, limit: $limit, after: $after) {
        invitations {
          ...InvitationFragment
          __typename
        }
        pageInfo {
          ...PageInfoFragment
          __typename
        }
        __typename
      }
    }

    fragment InvitationFragment on Invitation {
      id
      expiry
      to
      created
      from {
        ...ProfileFragment
        __typename
      }
      target {
        ...InvitationTargetFragment
        __typename
      }
      __typename
    }

    fragment ProfileFragment on Profile {
      __typename
      id
      alias
      picture
    }

    fragment InvitationTargetFragment on InvitationTarget {
      __typename
      ... on Team {
        id
        name
        __typename
      }
      ... on Video {
        id
        name
        __typename
      }
    }

    fragment PageInfoFragment on QueryPageInfo {
      end
      more
      __typename
    }
  "
}
