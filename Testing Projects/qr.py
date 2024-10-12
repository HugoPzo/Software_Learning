import pyqrcode

from pyqrcode import QRCode

# String which represent the QR code
page = "https://youtube.com"

# Generate QR code
url = pyqrcode.create(page)

# Create 'svg' image
# url.svg("name", scale=num)
url.svg("youtube.svg", scale=8)