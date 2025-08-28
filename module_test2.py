# import Mypackage_museum.mymodule2 as mymodule2
from Mypackage_museum.mymodule2 import get_artist

def main():
    artist = input("Artist: ").strip().title() 
    limit = int(input("Limit: "))
    artists = get_artist(query=artist,limit=limit)
    i=0 
    for artist in artists:
        print(f"{i+1}. {artist}") 
        i+=1

if __name__ == "__main__":
    main() 