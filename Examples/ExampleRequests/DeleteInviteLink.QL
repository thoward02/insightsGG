{
"operationName":"DeleteInvitationMutation",
"variables":{
  "input":{
    "teamId":"68ADJyplPEM1EwcV11gfGp",
    "invitationId":"6PLlmZIUpAHwSTOmPPxaHi"
    }
  },
  "query":"mutation DeleteInvitationMutation($input: DeleteInvitationInput!) {
    deleteInvitation(input: $input) {
      id
      __typename
    }
  }
"
}
