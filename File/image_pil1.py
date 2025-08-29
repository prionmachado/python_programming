from PIL import Image, ImageFilter 

def main():
    with Image.open("File/in.jpeg") as img:
        #print(img.format, img.size, img.mode) 
        img = img.rotate(180)
        # img.filter(ImageFilter.BLUR)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("File/out.jpeg") 

main() 