{
"operationName":"UntagVideoMutation",
"variables":{
  "input":{
    "videoId":"12fTaEbbNwNIV2oaDP6ILn",
    "tagIds":["6umxsSgaCzt5o2eKazUr5"]
    }
},
"query":"mutation UntagVideoMutation($input: UntagVideoInput!) {
    untagVideo(input: $input) {
      video {
        id
        tags
        __typename
      }
      __typename
    }
  }
  "
}
