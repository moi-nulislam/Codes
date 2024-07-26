import os
import qrcode

def main():
    img = qrcode.make(input("Enter link: "))
    img.save("qr.png", "PNG")

    os.system("start qr.png")

main()
