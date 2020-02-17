import insightsGG
from datetime import datetime

x = datetime.now()

App = insightsGG.App()

Login = App.Login("audaciousxth@gmail.com", "stevesmells")

print(App.User)
