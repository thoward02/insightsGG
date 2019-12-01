{
"operationName":"CreateRoleMutation",
"variables":{
  "input":{
    "name":"Players",
    "teamId":"68ADJyplPEM1EwcV11gfGp",
    "privileges":["CREATE_VOD","UPDATE_VOD","DELETE_VOD","CREATE_TAG","UPDATE_TAG","DELETE_TAG","ASSIGN_TAG","UPDATE_COMMENT","CREATE_COMMENT","UPDATE_ROLE","REMOVE_MEMBER","CREATE_ROLE","ASSIGN_ROLE","START_SESSION"],
    "color":"rgb(255, 97, 95)"
  }
},
"query":"mutation CreateRoleMutation($input: CreateRoleInput!) {
    createRole(input: $input) {
      role {
        ...RoleFragment
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
  "
}
