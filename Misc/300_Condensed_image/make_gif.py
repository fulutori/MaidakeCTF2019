from PIL import Image, ImageDraw, ImageFont

images = []
width = 300
color = (0, 0, 0)
flag = "MaidakeCTF{gif_has_more_than_one_picture_concatenated}"

for moji in flag:
	img = Image.new('RGB', (width, width), color)
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 230)
	draw.text((80,30), moji, font=font)
	images.append(img)

images[0].save('flag.gif', save_all=True, append_images=images[1:], optimize=False, duration=10, loop=0)