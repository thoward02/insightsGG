{
  "operationName":"CreateAnalysisRequestMutation",
  "variables":{
    "input":{
      "type":"OVERWATCH",
      "videoId":"FPc1psj7bPZ4B9kUjM9M0"
    }
  },
  "query":"mutation CreateAnalysisRequestMutation($input: CreateAnalysisRequestInput!) {
      createAnalysisRequest(input: $input) {
        analysis {
          ...AnalysisFragment
          __typename
        }
        __typename
      }
    }

    fragment AnalysisFragment on Analysis {
      id
      type
      created
      completed
      progress {
        current
        rate
        total
        __typename
      }
      result {
        matches {
          id
          __typename
        }
        __typename
      }
      error
      __typename
    }
    "
}
