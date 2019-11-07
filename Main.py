#import class
import Insights


App = Insights.App("EMAIL", "PASSWORD")

App.Login()

ExampleData = """[{"operationName":"GetOverwatchPrimaryRosterPlayerStatisticsV2Query","variables":{"teamId":"3TgFASLSgVEEGepquSDe95","videoIds":["jUNsJivlBFWwT45L6kY3g"]},"query":"query GetOverwatchPrimaryRosterPlayerStatisticsV2Query($teamId: ID, $videoIds: [ID!]) {  statistics(teamId: $teamId, type: OVERWATCH, videoIds: $videoIds) {    ... on OverwatchStatistics {      __typename      primaryRosterV2 {        name        players {          ...OverwatchPlayerStatisticsV2Fragment          __typename        }        __typename      }    }    __typename  }}fragment OverwatchPlayerStatisticsV2Fragment on OverwatchPlayerStatisticsV2 {  playerId  playerName  kills  deaths  ults  time  firstDeaths  firstKills  firstUlts  assists  heroes {    ...OverwatchPlayerHeroStatisticsFragment    __typename  }  __typename}fragment OverwatchPlayerHeroStatisticsFragment on OverwatchPlayerHeroStatistics {  name  teamfights  firstKills  firstDeaths  ults  firstUlts  totalChargeTime  numUltCharge  totalHoldTime  time  kills  deaths  assists  __typename}"}]"""


print(App.MakeRequest(ExampleData))
