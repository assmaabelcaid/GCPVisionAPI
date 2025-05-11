from PIL import Image

# Coordinates from your crop hint
vertices = [
    (0, 36),
    (647, 36),
    (647, 400),
    (0, 400)
]

# Define the bounding box for cropping
left = vertices[0][0]
top = vertices[0][1]
right = vertices[2][0]
bottom = vertices[2][1]
cropping_box = (left, top, right, bottom)

try:
    # Open the image
    img = Image.open(r'.\images\brrbrrpatapim.png')  # Replace your_image.jpg" with the actual path

    # Crop the image
    cropped_img = img.crop(cropping_box)

    # Save the cropped image
    cropped_img.save(".\images\cropped_image.png")
    print("Image cropped and saved as cropped_image.png")

except FileNotFoundError:
    print("Error: Image file not found.")
except Exception as e:
    print(f"An error occurred: {e}")