from PIL import Image
import numpy as np

first = Image.open('first.png')
second = Image.open('second.png')
third = Image.open('third.png')

width, height = first.size
first_pixels = np.array([[first.getpixel((i,j)) for j in range(height)] for i in range(width)])
second_pixels = np.array([[second.getpixel((i,j)) for j in range(height)] for i in range(width)])
third_pixels = np.array([[third.getpixel((i,j)) for j in range(height)] for i in range(width)])

def make_flag(image_size, bg, file_name):
	img = Image.new('RGB', image_size, bg)
	for i in range(image_size[0]):
		for j in range(image_size[1]):
			img.putpixel((i, j), (first_pixels[i][j], second_pixels[i][j], third_pixels[i][j]))
	img.save(file_name)
			

if __name__ == '__main__':
	image_size = (width, height)
	bg = (255, 255, 255)

	file_name = 'flag.png'

	make_flag(image_size, bg, file_name)