import json

from datetime import datetime
now = datetime.now() # current date and time
currentDate = now.strftime("%m/%d/%Y_%H:%M:%S")

import requests

wiki_req = ["Random wiki of the day","Can you link me to a random wiki", "Wiki"]
wiki_res= []

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "random",
    "rnlimit": "5"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

RANDOMS = DATA["query"]["random"]

for r in RANDOMS:
    wiki_res.append("'"+r["title"]+"'")

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

append_statistics('./intents.json', currentDate,wiki_req,wiki_res)