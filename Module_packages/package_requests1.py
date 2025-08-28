import requests 
# import json 
import sys

def main():
    print("Search the Art Institute of Chicago !") 
    print() 
    artist = input("Enter artist name: ") 
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q":artist}  
        )   
        response.raise_for_status() 
    except requests.HTTPError:
        print("Couldn't complete request")
        sys.exit() 

    # print(json.dumps(response.json(),indent=4)) 
    response = response.json() 
    i = 0 
    for artwork in response["data"]:
        print(f"{i+1}. {artwork["title"]}") 
        i += 1 

main() 