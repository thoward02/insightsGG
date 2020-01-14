# InsightsGG
This is the unofficial python API Wrapper for [Insights.gg](https://insights.gg/)
<br />
This wrapper gives you programatic access to *most* of what insights has to offer in their platform. Some of it has been intentionally left out in order to prevent spam issues while the platform is still in its beta. 
<br />
That being sai, the stats portion of the API Wrapper is written around the premis that you do have an account with the site that has [PRO access](https://insights.gg/insights-pro), and are using this API for Overwatch. If you're looking to pull stats from smash, I'm sorry but I haven't dove into that section yet, but if you want me to, feel free to contact me C:

# Credits
All of the code is being written currently by Aud (with some fixes/additions by Aplox), who is currently pursuing a career in esports coaching. He primarily works Collegiate Overwatch, but has been on break helping the both the Path To Pro community and Collegiate get better. *(And he may or may not be trying to convince Stephen at Insights to let him come work there uwu)*
<br />
A lot of the API guidance has been from [HSL's Aplox](https://twitter.com/_aplox?lang=en) and [HSL's Josh](https://twitter.com/tschoschi90?lang=en). Huge thanks to those two, who orginally stumbled upon my work in a random channel, and came to me looking to pump out this API for the entire scene. They've been here every step of the way and have offered so much guidance.
<br />
As for the API Wrapper itself, while written all by Aud, there has been massive help from the **entire** insights team for answering the THOUSANDS of questions I've had about the program as a whole.  
<br />
Big thank yous to: 
<br />
Stephen and Kevin whom have both let me work with their team more and more, in hopes of really making Insights suceed. 
<br />
Steve for listening to my endless questions about the GraphQL API, and giving occassional feedback on my work 
<br />
Denning for explaining how portions of the machine learning section so that I may better understand the proccess itself
<br />
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
First off you'll need python which can be aqquired through `apt` (for debian linux users) or [Here](https://www.python.org/downloads/) for windows users 
<br />
After that you'll need to install the API Wrapper via the `pip` system by going into your terminal and running `python3 -m pip install insightsGG` or `py -m pip install insightsGG` if you're on windows

## Python Requirements
The only library you'll need is `requests`, which can be pip installed by `python3 -m pip install requests` on Linux, or `py -m pip install requests` on windows
<br />
**Note** *this should install when you install the API Wrapper via pip, but if you are manually installing you'll need to hand install the dependencies*

# Getting Started
## The Wiki 
When first getting started, it is highly recommened that you read into the (https://github.com/thoward02/insightsGG/wiki/)[Wiki] so that you understand how and why this wrapper was written. Knowing such will allow you to better understand the API Wrapper itself, and work more effiecently with it. 

## Examples
**NOTE: As of 01/14/20 I am unsure of which examples take which login format, so please bare with me as I attempt rewrite them on a later date. Keep this in mind when running and exploring the Examples, as some may require you to authenticate using your username and password as command line parameters, and some may not.**
<br />
Within this repository you'll find a Directory, or folder, named `Examples`, which contains all of the works I and the HSL Boys have done with the API Wrapper. These are included to give you an idea of how we're using the API Wrapper, in hopes that it'll familiarize you with the wrapper itself.

### Example Code
All of the files ending with `.py` are example programs that you can run, and their titles pretty much explain what they do. For example `FetchUserInfo.py` fetches the user info of what ever account you logged into, and prints it out. 
<br />
The `Output` directory or folder contains all of the file outputs of the example programs, for example: The example programs that push out CSV formatted data, saves it to that directory and the same applies for the JSON files.

<br />
All of the examples can be ran by inputting your username and password as parameters, for example: `python3 filename.py rawxd@ihatemyself.com OkBoomer`, where `rawrxd@ihatemyself.com` is the your login email, and `OkBoomer` is your login password.
<br />
The examples also have the ability to use a `login.json` structure to prevent the hassle of writing your username and password everytime you wish to log in. 
The `login.json` structure basically implies you create a file named `login.json` within the `Examples` directory of this repository, populate it with your login info, like so: 
```json
  {
    "username" : "email@domain.com",
    "password" : "yourinsightspassword"
  }
```


