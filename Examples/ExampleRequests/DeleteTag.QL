{
  "operationName":"DeleteTagMutation",
  "variables": {
    "input":{
      "id":"6fGgN27sNdk6zBgxkOafqv",
      "teamId":"3pBQbTOPFYwxVKIHPirMvF"
    }
  },
  "query":"mutation DeleteTagMutation($input: DeleteTagInput!) {
    deleteTag(input: $input) {
      tagId
      __typename
    }
  }
  "
}
