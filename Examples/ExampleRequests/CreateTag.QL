{
  "operationName":"CreateTagMutation",
  "variables":{
    "input":{
      "teamId":"3pBQbTOPFYwxVKIHPirMvF",
      "name":"UwU",
      "color":"rgb(190, 223, 68)"
    }
  },
  "query":"mutation CreateTagMutation($input: CreateTagInput!) {
      createTag(input: $input) {
        tag {
          ...TagFragment
          __typename
        }
        __typename
      }
    }

    fragment TagFragment on Tag {
      id
      name
      color
      __typename
    }
    "
}
