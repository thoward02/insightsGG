# Insights.ggApi
This is the unofficial python API for Insights.gg

# Demo Testing
  While the actual API class is located in `Src/Insights.py`, an example interface is written in `Src/TeamfightToCSV.py` to give you an example of what the API can actually do. It does essentially what the title says, converts team fights into CSV format. In order to get started with the demo, you'll first need to add a file to the `Src` folder titled "login.json", and fill it with a json object containing your email and password, like so.
  ```json
    {
      "username" : "email@domain.com",
      "password" : "yourinsightspassword"
    }
  ```
  Once that's done, you can just run the example program(s) C:
