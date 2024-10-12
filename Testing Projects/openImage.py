# Image Library - > pip install pillow
from PIL import Image

# Load an image (only: JPEG, PNG, BMP, GIF, and PPM)
img = Image.open('imagen.jpg')
# Display the image
img.show()