import os
import qrcode

def main():
    img = qrcode.make("https://www.youtube.com/watch?v=z9bZufPHFLU&list=PLfqMhTWNBTe0b2nM6JHVCnAkhQRGiZMSJ")
    img.save("qr.png", "PNG")

    os.system("start qr.png")

main()
