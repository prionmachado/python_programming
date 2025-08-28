import requests

def main():
    artwork = input("Artwork: ").strip().title()
    Limit = int(input("Limit: "))
    artworks = get_artworks(query=artwork, limit=Limit)
    i = 0
    for artwork in artworks:
        print(f"{i+1}. {artwork}")
        i += 1

def get_artworks(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": query, "limit": limit}
        )
        response.raise_for_status()
    except requests.HTTPError:
        return []
    content = response.json()
    return [artwork["title"] for artwork in content["data"]]

if __name__ == "__main__":
    main() 