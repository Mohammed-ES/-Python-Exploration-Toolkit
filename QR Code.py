# pip install pyqrcode
# pip install pypng
import pyqrcode
import png
from pyqrcode import QRCode

# String which represents the QR code
# URL contenant un message humoristique
s = "https://code.com"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg('myqr.svg', scale=8)

# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale=6)
print("QR code generated successfully")
