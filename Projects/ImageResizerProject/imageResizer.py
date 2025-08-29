import cv2

# Read the image
src = cv2.imread("Projects/batman.jpg", cv2.IMREAD_UNCHANGED)

# Check if image loaded correctly
if src is None:
    print("Error: Could not load image.")
    exit()

# Set scale percentage
scale_percent = 50

# Compute new dimensions
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# Resize the image
output = cv2.resize(src, (new_width, new_height)) 

# Save the resized image
cv2.imwrite("Projects/newImage.png", output)
print("Image saved as 'newImage.png'") 
