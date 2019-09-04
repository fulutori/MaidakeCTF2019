from PIL import Image

flag = []
with open('flag.csv', 'r') as f:
	for row in f.read().split('\n'):
		if row == '':
			continue
		row = list(map(int, row.split(',')))
		row_flag = []
		for i in range(0, len(row), 3):
			row_flag.append([row[i], row[i+1], row[i+2]])
		flag.append(row_flag)

width = len(flag[0])
height = len(flag)

img = Image.new('RGB', (width, height))
for idx_r, row in enumerate(flag):
	for idx_c, col in enumerate(row):
		r, g, b = col
		img.putpixel((idx_c, idx_r), (r, g, b))

img.save('flag.png')
