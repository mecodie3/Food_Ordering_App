import qrcode

#creating an image
image = qrcode.make("https://127.0.0.1:8000")
#name the image
image.save("qr.png")