from PIL import Image

f = open('flag.txt', 'r')
flag = f.readlines()

for i in range(len(flag)):
	flag[i] = list(map(int, flag[i].replace('\n', '').split(',')))

width = len(flag[0])
height = len(flag)

img = Image.new('RGB', (width, height))
for idx_r, row in enumerate(flag):
	for idx_c, col in enumerate(row):
		if col == 0:
			img.putpixel((idx_r, idx_c), (255, 255, 255))
		elif col == 1:
			img.putpixel((idx_r, idx_c), (0, 0, 0))

#img.show()
img.save('flag.png')