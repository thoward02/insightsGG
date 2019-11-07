#Imports
import requests

class App:
    #Login
    Username    = None
    Password    = None
    Token       = None

    LoginPath   = "https://insights.gg/oauth/token"


    #Requests
    RequestPath = "https://insights.gg/graphql"

    #Setup the class constructor
    def __init__(self, Username, Password):
        self.Username = Username
        self.Password = Password

    def Login(self):
        #Send login
        LoginRequest = requests.post(url = self.LoginPath, data={"username":self.Username, "password" : self.Password})

        #Pull Bearer token out of login request
        Return = LoginRequest.json()
        self.Token = Return["access_token"]

    def MakeRequest(self, UserRequest):
        Header = {"Authorization" : "Bearer " + self.Token, "content-type" : "application/json"}

        print(UserRequest)

        Request = requests.post(url = self.RequestPath, data=UserRequest, headers=Header)
        return Request.json()
