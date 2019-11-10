[
{"operationName":"GetTagsQuery","variables":{"teamId":"68ADJyplPEM1EwcV11gfGp"},"query":"query GetTagsQuery($teamId: ID, $limit: Int, $after: Cursor) {
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
"},{"operationName":"GetVideosQuery","variables":{"teamId":"68ADJyplPEM1EwcV11gfGp","limit":100},"query":"query GetVideosQuery($teamId: ID, $limit: Int, $after: Cursor) {
  queryVideos(teamId: $teamId, limit: $limit, after: $after) {
    videos {
      ...VideoFragment
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

fragment PageInfoFragment on QueryPageInfo {
  end
  more
  __typename
}
"},{"operationName":"GetMembersQuery","variables":{"teamId":"68ADJyplPEM1EwcV11gfGp"},"query":"query GetMembersQuery($teamId: ID!, $limit: Int, $after: Cursor) {
  queryMembers(teamId: $teamId, limit: $limit, after: $after) {
    edges {
      ...MemberFragment
      added
      __typename
    }
    pageInfo {
      ...PageInfoFragment
      __typename
    }
    __typename
  }
}

fragment MemberFragment on Member {
  id
  added
  nickname
  roles {
    id
    __typename
  }
  privileges
  user {
    ...ProfileFragment
    __typename
  }
  __typename
}

fragment ProfileFragment on Profile {
  __typename
  id
  alias
  picture
}

fragment PageInfoFragment on QueryPageInfo {
  end
  more
  __typename
}
"},{"operationName":"GetRolesQuery","variables":{"teamId":"68ADJyplPEM1EwcV11gfGp"},"query":"query GetRolesQuery($teamId: ID!, $limit: Int, $after: Cursor) {
  queryRoles(teamId: $teamId, limit: $limit, after: $after) {
    roles {
      ...RoleFragment
      __typename
    }
    pageInfo {
      ...PageInfoFragment
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
  __typename
}

fragment PageInfoFragment on QueryPageInfo {
  end
  more
  __typename
}
"}]
