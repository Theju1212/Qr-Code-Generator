import qrcode
from PIL import Image
import os  # Import os to check if the file exists

# Ask the user for input
data = input("Enter the text or URL for the QR Code: ")
fill_color = input("Enter QR code color (e.g., black, blue, red): ")
bg_color = input("Enter background color (e.g., white, yellow, pink): ")

# Create a QR code instance
qr = qrcode.QRCode(
    version=4,  
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction (important for logos)
    box_size=10,  
    border=4,  
)

# Add data to the QR Code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code
img = qr.make_image(fill=fill_color, back_color=bg_color).convert("RGB")

# Check if 'logo.png' exists
logo_path = "logo.png"
if os.path.exists(logo_path):
    # Open the logo image
    logo = Image.open(logo_path)

    # Resize the logo
    logo_size = img.size[0] // 5  # 1/5th of QR code size
    logo = logo.resize((logo_size, logo_size))

    # Calculate position to place the logo at the center
    pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)

    # Paste the logo onto the QR code
    img.paste(logo, pos, mask=logo)
else:
    print("⚠️ Logo file not found! QR code will be generated without a logo.")

# Save the QR code image
img.save("custom_qr_code_with_logo.png")

print("✅ QR Code generated and saved as custom_qr_code_with_logo.png")
