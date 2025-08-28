import requests 
import sys
import json 

if len(sys.argv) != 2:
    sys.exit() 

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=4)) 

# response1 = response.json()
# for result in response1["results"]:
#     print(result["trackName"])  