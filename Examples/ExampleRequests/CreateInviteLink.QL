{
  "operationName":"CreateInvitationMutation",
  "variables":{
    "input":{
      "teamId":"68ADJyplPEM1EwcV11gfGp",
      "expiry":"P5D",
      "limit" :5

    }
  },
  "query":"mutation CreateInvitationMutation($input: CreateInvitationInput!) {
      createInvitation(input: $input) {
        invitation {
          ...Invitation2Fragment
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
    "
}
