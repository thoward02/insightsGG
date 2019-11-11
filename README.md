# InsightsGG
This is the unofficial python API for [Insights.gg](https://insights.gg/)
The API is written around the idea that you do have an account with the site that has [PRO access](https://insights.gg/insights-pro), and are using this API for Overwatch. If you"re looking to pull stats from smash, I"m sorry but I haven"t dove into that section yet, but if you want me to, feel free to contact me C:

# Credits
All of the code is being written currently by Aud, who is currently pursuing a career in esports coaching, and works in the OW Collegiate scene and does pick up coaching.

A lot of the API guidance has been from [HSL"s Aplox](https://twitter.com/_aplox?lang=en) and [HSL"s Josh](https://twitter.com/tschoschi90?lang=en). Huge thanks to those two, who came to me looking to pump out this API for the entire scene. They"ve been here every step of the way and have offered so much guidance.

As for the API itself, while written all by Aud, there has been massive help from Norapuro at insights for answering the THOUSANDS of questions I"ve had about the program as a whole.  

If you have any questions at all feel free to hit the HSL boys or I up:
```Javascript
//Aud
Aud#9488
https://twitter.com/mrcoachaud
//Aplox
Aplox#2681
https://twitter.com/_aplox
//Josh
Tschoschi#0979
https://twitter.com/tschoschi90
```

# Before you get started

## Basic install
You can easily install via the pip system, by going into your terminal and running `python3 -m pip install insightsGG` or `py -m pip install insightsGG` if you"re on windows

## Python Requirements
The only library you"ll need is `requests`, which can be pip installed by `python3 -m pip install requests` on Linux, or `py -m pip install requests` on windows *Note this should install when you install via pip, but if you are manually installing you"ll need to hand install the dependencies*

## Login Requirements
All of the examples can be ran by inputting your username and password as parameters, for example: `python3 filename.py rawxd@ihatemyself.com OkBoomer`, where `rawrxd@ihatemyself.com` is the your login email, and `OkBoomer` is your login password.

The examples also have the ability to use a `login.json` structure to prevent committing usernames and passwords. If you wish to run an example through this login structure either:
create a file in the same directory as the program named `login.json` and populate it with the following data
```json
  {
    "username" : "email@domain.com",
    "password" : "yourinsightspassword"
  }
```

or

Modify the example files and hand input your login information into the `Login` function.


# The API
The api is a reversed engineered product of the insights.gg website, that is still in development big time. `App.py` is the main library file, and contains everything you need to know about the API. If you understand python this shouldn"t be too hard to understand.

That being said I"ll go ahead and lay out some specifics as of right now.
## Oh dear god it"s written awfully
So this current version was written in about 18 hours, give or take 4 hours, so go easy on me. I wrote fast and sloppy in order to get out a basic version **that"s useable**. At this moment you can get all of the data you want out of insights using the API, thus it"s technically finished. That being said, I plan on fixing all the messy code, and making things easier on you. As of right now everything is stored in one file, and is not documented as well as it needs to be, so don"t fret I will be updating things C:

# How the API works
## Connecting with insights.gg
Insights follows your typical REST API structure, meaning that all we need to do is make HTTPS post request to various URLs in order to get the data we need. All of this was written by *"reverse engineering"* the website, so all of the post requests remain identical to how the normal client makes them as well.

### Login
Logging in is a simple POST request to `https://insights.gg/oauth/token`, containing the data
```json
{
  "username" : "String",
  "password" : "String"
}
```
If the username and password were both correct, the site will then return a bearer token in the following json format
```json
{
  "token_type"   : "Bearer",
  "expires_in"   : -1,
  "access_token" : "key"
}
```
The access token is how you"ll make requests to insights.gg so if you"re not following my API, ensure you save that globally, for you"ll need it to authenticate every request you make.


Thankfully this is all taken care of in `App.py` during the `Login(Username, Password)` function, and the token is saved in the `Token` variable inside of `App`. The login function then takes that token and then requests for your user information, which is stored in `User` inside of `App` in the following json format:
```json
{
  "id": "USERID",
  "name": "USERNAME",
  "email": "USEREMAIl",
  "alias": "USERALIAS",
  "picture": "LinkToUserPicure",
  "verified": true,
  "whitelisted": true,
  "marketing": true,
  "updates": true
}
```
Most of the variables are pretty self explanatory, apart from the last 4. Verified implies user has verified their email address, whitelisted implies ?? (*note double check with insights dev as to what this means lol*), marketing and updates are both flags on whether a user will be emailed about insights updates // additions.
After storing the user information, the API then grabs a list of the users teams, and stores them in `Teams`, in the json format:
```json
{
  "Team_Name": {
    "id": "Team_Id",
    "description": "This is where your team description is",
    "owner": "TeamOwner",
    "VodList": {
      "VodName": {
        "id": "VodId",
        "created": "2019-10-24T19:24:03.833853Z",
        "filesize": 0,
        "name": "VodName",
        "streamUrl": "A Link to the stored video",
        "remoteUrl": "A link to the outside video",
        "error": null,
        "thumbnail": "Video thumbnail",
        "progress": {
          "current": 1,
          "rate": 0,
          "total": 1
        },
        "uploaded": "True",
        "tags": [
          "TagIds"
        ],
        "duration": 7716.408,
        "comments": "True",
        "public": "True",
        "owner": {
          "id": "OwnerId",
          "name": "TeamName",
          "picture": "TeamPicture"
        },
        "userMetadata": [],
        "latestAnalysis": {
          "id": "AnalysisId",
          "type": "OVERWATCH",
          "created": "2019-11-08T00:44:27.632394Z",
          "completed": "2019-11-08T00:51:25.03306Z",
          "progress": {
            "current": 1,
            "rate": 0,
            "total": 1,
            "__typename": "Progress"
          },
          "result": {
            "matches": [
              {
                "id": "MatchId"
              }
            ]
          }
        }
      },
    }
  }
}
```
So yeah that's a lot of data **per team**, and that's trimmed down. An example request of some teams can be upwards 100kb depending on how many vods are stored, length of vods etc etc. Now you're probably wondering why the server would return all that data right? Well insights.gg uses GraphQL for their front end system, which means the server only returns what the user asks for. If you've never heard of GraphQL, take a moment to look it up, it's a super neat system.
That being said, we got all that data because we requested all of it, which is a critical flaw of this API system as of right now, for there's no current way to edit the API requests to only grab specific data, like just the team ids, or what have you. This is due to my lack of knowledge on GraphQL, however I'm working hard to learn how GraphQL works so please bear with me.
Essentially I've just copied how the client makes request, thus we get all of the data the client needs, including all the rubbish. It's like learning how to write, only by copying other people's writing. Sure you can technically write, but you can't write your own thoughts, only a mesh of other people's words.

After grabbing the team name list, the API then goes back and writes over the "VodList" dict with a list of all the videos within a team, this way we don't have to make extra requests later on, which is shown in the example above as well. Then the API is done officially logging in.

### Working with the data
PART TWO INCOMING WHEN I'VE GOT TIME
