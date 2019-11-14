# InsightsGG
This is the unofficial python API for [Insights.gg](https://insights.gg/)
The API is written around the idea that you do have an account with the site that has [PRO access](https://insights.gg/insights-pro), and are using this API for Overwatch. If you're looking to pull stats from smash, I'm sorry but I haven't dove into that section yet, but if you want me to, feel free to contact me C:

# Credits
All of the code is being written currently by Aud (with some fixes by Aplox), who is currently pursuing a career in esports coaching, and works in the OW Collegiate scene and does pick up coaching.

A lot of the API guidance has been from [HSL's Aplox](https://twitter.com/_aplox?lang=en) and [HSL's Josh](https://twitter.com/tschoschi90?lang=en). Huge thanks to those two, who came to me looking to pump out this API for the entire scene. They've been here every step of the way and have offered so much guidance.

As for the API itself, while written all by Aud, there has been massive help from Norapuro at insights for answering the THOUSANDS of questions I've had about the program as a whole.  

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
You can easily install via the pip system, by going into your terminal and running `python3 -m pip install insightsGG` or `py -m pip install insightsGG` if you're on windows

## Python Requirements
The only library you'll need is `requests`, which can be pip installed by `python3 -m pip install requests` on Linux, or `py -m pip install requests` on windows *Note this should install when you install via pip, but if you are manually installing you'll need to hand install the dependencies*

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



