{
  "operationName":"RemoveMemberMutation",
  "variables":{
    "input":{
      "teamId":"68ADJyplPEM1EwcV11gfGp",
      "memberId":"3Foy8u99E71NOTJKRovkdv"
      }
    },
  "query":"mutation RemoveMemberMutation($input: RemoveMemberInput!) {
      removeMember(input: $input) {
        memberId
        __typename
      }
    }
    "
}
