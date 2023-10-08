import qrcode
from PIL import Image
import cv2
d="ram"
qr=qrcode.QRCode(version=1,box_size=10,border=4)
qr.add_data(d)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img.save("ram.png")