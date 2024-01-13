import requests
import json

class GetRequester:
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    def __init__(self, url):
        self.url = url
       

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        dict_list = []
        body = self.get_response_body()
        data = json.loads(body)

        for entry in data:
            name = entry["name"]
            occupation = entry["occupation"]
            dict_list.append(f"{name}{occupation}")

        return dict_list

names = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
all_data = names.load_json()

for entry in all_data:
    print(entry)