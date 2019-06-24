from PIL import Image
import numpy as np

f_name = 'qr.png'
img = Image.open(f_name)

width, height = img.size
img_pixels = np.array([[img.getpixel((i,j)) for j in range(height)] for i in range(width)])

with open('flag.txt', 'w') as f:
	for row in img_pixels:
		for idx, col in enumerate(row):
			if col == 255:
				if idx == width-1:
					f.write('0\n')
				else:
					f.write('0,')
			elif col == 0:
				if idx == width-1:
					f.write('1\n')
				else:
					f.write('1,')