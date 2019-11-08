[
{"operationName":"GetVideosByIdQuery","variables":{"ids":["1scO9ipC61xQipHiWATlOS"]},"query":"query GetVideosByIdQuery($ids: [ID!]!) {
  videos(ids: $ids) {
    ...VideoFragment
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
  progress {
    current
    rate
    total
    __typename
  }
  uploaded
  tags
  duration
  comments
  public
  owner {
    ...OwnerFragment
    __typename
  }
  userMetadata {
    ...MetadataEntryFragment
    __typename
  }
  latestAnalysis {
    ...AnalysisFragment
    __typename
  }
  __typename
}

fragment OwnerFragment on Owner {
  __typename
  ... on Self {
    name
    alias
    email
    picture
    __typename
  }
  ... on Profile {
    alias
    picture
    __typename
  }
  ... on Team {
    id
    name
    picture
    __typename
  }
}

fragment MetadataEntryFragment on MetadataEntry {
  name
  value
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
"},

{"operationName":"GetMatchesByIdQuery",
"variables":{"ids":["2HyM0p0pgETw5QlTIJ3Ia"]},
"query":"query GetMatchesByIdQuery($ids: [ID!]!) {
  matches(ids: $ids) {
    ...MatchFragment
    __typename
  }
}

fragment MatchFragment on Match {
  __typename
  id
  created
  owner {
    ...OwnerFragment
    __typename
  }
  name
  userMetadata {
    name
    value
    __typename
  }
  ... on UserMatch {
    video {
      id
      __typename
    }
    startTime
    endTime
    __typename
  }
  ... on GeneratedOverwatchMatch {
    gvideo: video {
      id
      __typename
    }
    analysis {
      id
      __typename
    }
    gstartTime: startTime
    gendTime: endTime
    data
    __typename
  }
}

fragment OwnerFragment on Owner {
  __typename
  ... on Self {
    name
    alias
    email
    picture
    __typename
  }
  ... on Profile {
    alias
    picture
    __typename
  }
  ... on Team {
    id
    name
    picture
    __typename
  }
}
"},{"operationName":"GetTagsQuery","variables":{"teamId":"3TgFASLSgVEEGepquSDe95"},"query":"query GetTagsQuery($teamId: ID, $limit: Int, $after: Cursor) {
  queryTags(teamId: $teamId, limit: $limit, after: $after) {
    tags {
      ...TagFragment
      __typename
    }
    pageInfo {
      ...PageInfoFragment
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

fragment PageInfoFragment on QueryPageInfo {
  end
  more
  __typename
}
"}]
