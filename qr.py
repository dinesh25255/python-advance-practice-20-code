import qrcode as qr

#when we generate qr code that time we install import qrcode and also we used and install pillow


img = qr.make("https://www.youtube.com/@ittrainingnepal-fu5mz")
img.save("ittrainingnepal_youtube.png")
