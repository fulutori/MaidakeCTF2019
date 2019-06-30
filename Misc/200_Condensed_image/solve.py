from PIL import Image, ImageSequence
import os

org_gif = 'flag.gif'
dic = 'image'

img = Image.open(org_gif)
frames = (frame.copy() for frame in ImageSequence.Iterator(img))

if not os.path.isdir(dic):
	os.mkdir(dic)

for i, f in enumerate(frames):
	name = '{}/{}.png'.format(dic, i+1)
	f.save(name)
