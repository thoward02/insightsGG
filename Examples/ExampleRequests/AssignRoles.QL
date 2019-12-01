{
  "operationName":"AddMemberRolesMutation",
  "variables":{
    "input":{
      "teamId":"68ADJyplPEM1EwcV11gfGp",
      "memberId":"3Foy8u99E71NOTJKRovkdv",
      "roles":[{"name":"gfx","global":false}]
    }
  },
  "query":"mutation AddMemberRolesMutation($input: AddMemberRolesInput!) {
      addMemberRoles(input: $input) {
        member {
          ...MemberFragment
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
    "
}
