from PIL import Image
import os

im = Image.open('flag.png')
size =im.size

for i in range(60):
	for n in range(2):

		bun = []
		for y in range(size[1]):
			for x in range(size[0]):
				bun.append(im.getpixel((x, y))[0])
		for y in range(size[1]):
			for x in range(size[0]):
				bun.append(im.getpixel((x, y))[1])
		for y in range(size[1]):
			for x in range(size[0]):
				bun.append(im.getpixel((x, y))[2])

		j=0
		for y in range(size[1]):
			for x in range(size[0]):
				r = bun[j]
				g = bun[j+1]
				b = bun[j+2]
				j = j + 3
				im.putpixel((x, y),( r,g,b))

	im.save("./img/{}.png".format(i+1))
