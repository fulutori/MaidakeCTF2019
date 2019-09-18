from PIL import Image
import numpy as np

img = Image.open('flag.jpg')
width, height = img.size
img_pixels = np.array([[img.getpixel((i,j)) for j in range(height)] for i in range(width)])

with open('flag.csv', 'w') as f:
	for y in range(height):
		for x in range(width):
			r, g, b = img_pixels[x][y]
			f.write('{},{},{}'.format(r, g, b))
			if x == width-1:
				f.write('\n')
			else:
				f.write(',')
