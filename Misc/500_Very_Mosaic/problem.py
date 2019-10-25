from PIL import Image
import os, tkinter.filedialog, tkinter.messagebox

im = Image.open('shigure.png')
size =im.size

for i in range(50):
	for n in range(2):

		bun = []
		for y in range(size[1]):
			for x in range(size[0]):
				bun.append(im.getpixel((x, y))[0])
				bun.append(im.getpixel((x, y))[1])
				bun.append(im.getpixel((x, y))[2])

		j=0
		for y in range(size[1]):
			for x in range(size[0]):
				r = bun[j]
				g = bun[j + len(bun)//3]
				b = bun[j + len(bun)//3 * 2]
				im.putpixel((x, y), (r, g, b))
				j=j+1

im.save("flag.png")
