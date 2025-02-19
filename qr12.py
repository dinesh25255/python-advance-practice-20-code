import qrcode
from PIL import Image

# Create QRCode object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data("https://softvista-creations.vercel.app/")
qr.make(fit=True)

# Create an image with custom colors
img = qr.make_image(fill_color="pink", back_color="blue")  # Changed fill_color to pink

# Save the QR code image with a proper file extension
img.save("softvistacreations.png")  # Added '.png' extension

# Show the QR code image (optional)
img.show()
