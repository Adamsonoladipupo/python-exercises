import qrcode

name = input("Enter website: ")

img = qrcode.make(f"{name}")
img.save(f"semicolon.png")
