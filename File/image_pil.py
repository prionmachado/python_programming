import sys 
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "File/costumes.gif",save_all=True, append_images=[images[1]],duration=200, loop=0 #infinite loop
    ) 
# Close all opened images
for image in images:
    image.close() 