# InsightsGG
This is the unofficial python API for Insights.gg


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


# The API
The api is a reversed engineered product of the insights.gg website, that is still in development big time. `App.py` is the main library file, and contains everything you need to know about the API. If you understand python this shouldn't be too hard to understand.

If you don't uh... Hold on, I'm going to write a detailed API to make things easier C:
