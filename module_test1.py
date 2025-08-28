# import Mypackage_museum.mymodule as mymodule1
from Mypackage_museum.mymodule1 import get_artworks

def main():
    artwork = input("Artwork: ").strip().title() 
    limit = int(input("Limit: "))
    artworks = get_artworks(query=artwork,limit=limit)
    i=0 
    for art in artworks:
        print(f"{i+1}. {art}") 
        i+=1

if __name__ == "__main__":
    main()  