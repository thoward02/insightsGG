{
  "operationName":"DeleteVideoMutation",
    "variables": {
      "input":{"id":"6smTjWNaqDgPsuXIrbpSqx"
      }
    },
  "query":"mutation DeleteVideoMutation($input: DeleteVideoInput!) {
      deleteVideo(input: $input) {
        videoId
        __typename
      }
    }"
}
