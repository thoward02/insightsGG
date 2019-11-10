[
{"operationName":"GetUserProfileQuery","variables":{},"query":"query GetUserProfileQuery {
  me {
    ...SelfFragment
    __typename
  }
}

fragment SelfFragment on Self {
  id
  name
  email
  alias
  picture
  verified
  whitelisted
  marketing
  updates
  __typename
}
"}]
