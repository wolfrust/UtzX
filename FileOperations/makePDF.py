import os
from sys import argv

if '--optimize' in argv:
	optimize = True
	print("[*] Optimization ON")
else:
	optimize = False

if '--quality' in argv:
	quality = argv[argv.index('--quality') + 1]
	print(f"[*] Custom Quality {quality}")
else: 
	quality = None
print()


FILES_IN_DIR = os.listdir()
IMAGES_IN_DIR = [f for f in FILES_IN_DIR if f.endswith(".jpg") or f.endswith(".png")]
IMAGE_NUMBER_REL = {}

for i in range(1, len(IMAGES_IN_DIR)+1):
    print(f"[{i}] {IMAGES_IN_DIR[i-1]}")
    IMAGE_NUMBER_REL[i] = IMAGES_IN_DIR[i-1]

CHOICE = input("Enter images to add, in order (eg.1,4,3,2): ").split(',')
CHOICE = [IMAGE_NUMBER_REL[int(i)] for i in CHOICE]

from PIL import Image #pillow

IMAGES = [Image.open(i) for i in CHOICE]
IMAGES = [i.convert('RGB') for i in IMAGES]


PDFNAME = input("Enter desired name of pdf file (without .pdf): ")

if quality is None:
	IMAGES[0].save(f"{PDFNAME}.pdf", save_all=True, append_images=IMAGES[1:len(IMAGES)], optimize=optimize)
else:
	IMAGES[0].save(f"{PDFNAME}.pdf", save_all=True, append_images=IMAGES[1:len(IMAGES)], optimize=optimize, quality=quality)



