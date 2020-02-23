{
  "operationName":"GetRolesQuery",
  "variables":{
    "teamId" : "TEAMID"
    "limit"  : "10"
    "after"  : ""
  },
  "query":"query GetTagsQuery($teamId: ID, $limit: Int, $after: Cursor){
      queryTags(teamId: $teamId, limit: $limit, after: $after){
          tags {
              ...TagFragment
          }
          pageInfo {
              ...PageInfoFragment
          }
      }
  }"
}
