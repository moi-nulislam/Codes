import os
import qrcode

def main():
    img = qrcode.make("Enter link here: ")
    img.save("qr.png", "PNG")

    os.system("start qr.png")

main()
