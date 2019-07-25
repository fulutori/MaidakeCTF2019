from PIL import Image
import os
import sys
import random

def ImgSplit(img, width, height):
	split = 4
	split_height = height // split
	split_width = width // split

	buff = []
	for h1 in range(split):
		for w1 in range(split):
			w2 = w1 * split_height
			h2 = h1 * split_width
			c = img.crop((w2, h2, split_width + w2, split_height + h2))
			buff.append(c)
	return buff



if __name__ == '__main__':
	path = './puzzle/'
	if not os.path.isdir(path):
		os.makedirs(path)
	img = Image.open('qr.png')
	width, height = img.size
	puzzles = ImgSplit(img, width, height)
	last_puzzle = puzzles[-1]
	puzzles = puzzles[:-1]
	random.shuffle(puzzles)
	puzzles.append(last_puzzle)
	
	
	for idx, puzzle in enumerate(puzzles):
		puzzle.save("{}{}.png".format(path,idx+1), "PNG")

