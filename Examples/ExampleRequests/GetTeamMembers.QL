{
  "operationName":"GetMembersQuery",
  "variables":{
    "teamId":"68ADJyplPEM1EwcV11gfGp"
  },
  "query":"query GetMembersQuery($teamId: ID!, $limit: Int, $after: Cursor) {
    queryMembers(teamId: $teamId, limit: $limit, after: $after) {
      edges {
        ...MemberFragment
        added
        __typename
      }
      pageInfo {
        ...PageInfoFragment
        __typename
      }
      __typename
    }
  }

  fragment MemberFragment on Member {
    id
    added
    nickname
    roles {
      id
      __typename
    }
    privileges
    user {
      ...ProfileFragment
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

  fragment PageInfoFragment on QueryPageInfo {
    end
    more
    __typename
  }
  "
}
