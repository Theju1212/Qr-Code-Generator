import os
from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def generate_qr():
    if request.method == "POST":
        data = request.form["data"]
        fill_color = request.form.get("fill_color", "black")  # Default to black
        bg_color = request.form.get("bg_color", "white")  # Default to white

        qr = qrcode.QRCode(
            version=4,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill_color, back_color=bg_color)

        # Save QR code to memory (for direct download)
        img_io = BytesIO()
        img.save(img_io, "PNG")
        img_io.seek(0)

        # Save QR code to static folder (for preview)
        img_path = "static/qr_code.png"
        img.save(img_path)

        return render_template("index.html", qr_code=img_path, download=True)

    return render_template("index.html", qr_code=None, download=False)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get port from Render
    app.run(host="0.0.0.0", port=port, debug=True)
