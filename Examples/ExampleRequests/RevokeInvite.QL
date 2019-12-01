{
  "operationName":"RevokeInvitationMutation",
  "variables":{
  "input":{
    "invitation":{
      "id":"6wYPh2dYOX1CgSIi9DzIuG",
      "teamId":"68ADJyplPEM1EwcV11gfGp"
      }
    }
  },
  "query":"mutation RevokeInvitationMutation($input: RevokeInvitationInput!) {
      revokeInvitation(input: $input) {
        invitationId
        __typename
      }
    }
    "
}
