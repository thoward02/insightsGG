[
{
  "operationName":"CreateRemoteVideoMutation",
  "variables":{
    "input":{
      "remoteUrl":"https://www.youtube.com/watch?v=Kp7eSUU9oy8&list=RDz1kEyLSGeM8&index=10",
      "teamId":""
    }
  },
  "query":"mutation CreateRemoteVideoMutation($input: CreateRemoteVideoInput!) {
    createRemoteVideo(input: $input) {
      video {
        ...VideoFragment

      }

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

    }
    uploaded
    tags
    duration
    comments
    public
    owner {
      ...OwnerFragment

    }
    userMetadata {
      ...MetadataEntryFragment

    }
    latestAnalysis {
      ...AnalysisFragment

    }

  }

  fragment OwnerFragment on Owner {

    ... on Self {
      name
      alias
      email
      picture

    }
    ... on Profile {
      alias
      picture

    }
    ... on Team {
      id
      name
      picture

    }
  }

  fragment MetadataEntryFragment on MetadataEntry {
    name
    value

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

    }
    result {
      matches {
        id

      }

    }
    error

  }
"}
]
