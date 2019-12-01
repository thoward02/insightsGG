{
  "operationName":"UpdateVideoMutation",
  "variables": {
    "input":{
      "id":"6smTjWNaqDgPsuXIrbpSqx",
      "name":"o w o",
      "public":false
      }
    },
    "query":"mutation UpdateVideoMutation($input: UpdateVideoInput!) {
    updateVideo(input: $input) {
      video {
        ...VideoFragment
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
  "
}
