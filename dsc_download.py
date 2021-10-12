import wget
import datetime
import time
import glob
from PIL import Image
import os

#filepaths
fp_in="/root/DSCCam*.jpg"
fp_out="/root/dsc_loop/loop.gif"
image_url = 'https://remote.dsc.org.au/camera/DSCCam.jpg'

for i in range(8):
	image_filename = wget.download(image_url)
	print('Image Successfully Downloaded: ', image_filename)
	time.sleep(360)

img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=200, loop=0)

os.remove("/root/DSCCam.jpg")

for i in range(1,8):
	path="/root/DSCCam (%d).jpg" % (i)
	os.remove(path)
