{
"operationName":"UpdateTeamMutation",
"variables": {
  "input":{
    "id":"3pBQbTOPFYwxVKIHPirMvF",
    "name":"jjzzz"
  }
},
"query":"mutation UpdateTeamMutation($input: UpdateTeamInput!) {
    updateTeam(input: $input) {
      team {
        ...TeamFragment
        __typename
      }
      __typename
    }
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
