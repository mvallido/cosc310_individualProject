import json

from datetime import datetime
now = datetime.now() # current date and time
currentDate = now.strftime("%m/%d/%Y_%H:%M:%S")

import wolframalpha

appID = "KJ4XP9-8VGKLGE8PK"
client = wolframalpha.Client(appID)
res = client.query("What is the weather")
answer = next(res.results).text

wolf_req = ["What is the weather today","weather", "Todays weather"]
wolf_res= [answer]

def append_statistics(filepath, date, input, output):

    with open(filepath, 'r') as fp:
        information = json.load(fp)

    information["intents"].append({
        "tag": date,
        "patterns": input,
        "responses": output
    })

    with open(filepath, 'w') as fp:
        json.dump(information, fp, indent=2)

append_statistics('./intents.json', currentDate, wolf_req, wolf_res)