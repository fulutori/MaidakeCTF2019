from PIL import Image
import numpy as np
import io
import zbarlight

flag = Image.open('flag.png')

width, height = flag.size
flag_pixels = np.array([[flag.getpixel((i,j)) for j in range(height)] for i in range(width)])


def make_flag(image_size, bg):
	img1 = Image.new('RGB', image_size, bg)
	img2 = Image.new('RGB', image_size, bg)
	img3 = Image.new('RGB', image_size, bg)

	for i in range(image_size[0]):
		for j in range(image_size[1]):
			img1.putpixel((i, j), (flag_pixels[i][j][0], flag_pixels[i][j][0], flag_pixels[i][j][0]))
			img2.putpixel((i, j), (flag_pixels[i][j][1], flag_pixels[i][j][1], flag_pixels[i][j][1]))
			img3.putpixel((i, j), (flag_pixels[i][j][2], flag_pixels[i][j][2], flag_pixels[i][j][2]))
	
	img1.save('flag1.png')
	img2.save('flag2.png')
	img3.save('flag3.png')

def get_qr():
	with open('flag1.png', 'rb') as f:
		image1= Image.open(io.BytesIO(f.read()))
	with open('flag2.png', 'rb') as f:
		image2= Image.open(io.BytesIO(f.read()))
	with open('flag3.png', 'rb') as f:
		image3= Image.open(io.BytesIO(f.read()))
	
	result1 = zbarlight.scan_codes('qrcode', image1)[0].decode()
	result2 = zbarlight.scan_codes('qrcode', image2)[0].decode()
	result3 = zbarlight.scan_codes('qrcode', image3)[0].decode()

	print(result1)
	print(result2)
	print(result3)


if __name__ == '__main__':
	image_size = (width, height)
	bg = (255, 255, 255)

	make_flag(image_size, bg)
	get_qr()