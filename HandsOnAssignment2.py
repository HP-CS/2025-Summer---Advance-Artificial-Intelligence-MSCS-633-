import qrcode
from PIL import Image

def generate_qr(url, output_file="qr_output.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    img.show()  # Display the QR image in a window

if __name__ == "__main__":
    input_url = input("Enter the URL to generate a QR code: ")
    generate_qr(input_url)
