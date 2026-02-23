import qrcode

url = input("Enter a URL: ").strip()
file_path = "C:\\Users\\Ameer\\Downloads\\qrcode\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR Code was generated!")