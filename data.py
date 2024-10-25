from xmlrpc.client import boolean

import requests

parameters = {
    "amount": 10,
    "type": "boolean",     #must use parenthesis around boolean
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
