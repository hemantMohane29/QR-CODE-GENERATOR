import qrcode

link = "https://drive.google.com/file/d/1nEghXGEXRgedjhfRekQh-RNkogIVvG32/view?usp=sharing"
qrcode.make(link).save("qr2.png")
print("QR generated: qr.png")
