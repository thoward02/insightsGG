{
  "operationName":"GetOWLVideosQuery",
  "variables":{
    "week":1,
    "year":2020,
    "limit":100
  },
  "query":"query GetOWLVideosQuery($week: Int!, $year: Int!, $limit: Int, $after: Cursor) {
    queryOWLVideos(week: $week, year: $year, limit: $limit, after: $after) {
      videos {
        ...VideoFragment
        latestAnalysis {
          result {
            matches {
              ...MatchFragment
              __typename
            }
            __typename
          }
          __typename
        }
        __typename
      }
      pageInfo {
        ...PageInfoFragment
        __typename
      }
      __typename
    }
  }

  fragment VideoFragment on Video {
    id
    created
    filesize
    name
    streamUrl
    remoteUrl
    error
    thumbnail
    latestAnalysis {
      ...AnalysisFragment
      __typename
    }
    __typename
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

  fragment PageInfoFragment on QueryPageInfo {
    end
    more
    __typename
  }

  fragment MatchFragment on Match {
    __typename
    id
    created
    name
    ... on GeneratedMatch {
      video {
        id
        __typename
      }
      analysis {
        id
        __typename
      }
      startTime
      endTime
      __typename
    }
    ... on GeneratedOverwatchMatch {
      owdata: data
      __typename
    }

  }"
}
