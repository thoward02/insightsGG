# Insights.ggApi
This is the unofficial python API for Insights.gg


# Before you get started

## Python Requirements
The only library you'll need is `requests`, which can be pip installed by `python3 -m pip install requests` on Linux, or `py -m pip install requests` on windows

## Login Requirements
Currently the examples use a `login.json` structure to prevent committing usernames and passwords. If you wish to run an example script either:
create a file in `Src` named `login.json` and populate it with the following data
```json
  {
    "username" : "email@domain.com",
    "password" : "yourinsightspassword"
  }
```

or

Modify the example files and hand input your login information into the `Login` function.


# The API
The api is a reversed engineered product of the insights.gg website, that is still in development big time. `Src/Insights.py` is the main library file, and contains everything you need to know about the API. If you understand python this shouldn't be too hard to understand.

If you don't uh... Hold on, I'm going to write a detailed API to make things easier C:
