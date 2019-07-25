from PIL import Image
import os
import sys

from datetime import datetime

def ImgSplit(im):
	# 読み込んだ画像を200*200のサイズで54枚に分割する
	height = 110
	width = 110

	buff = []
	# 縦の分割枚数
	for h1 in range(3):
		# 横の分割枚数
		for w1 in range(3):
			w2 = w1 * height
			h2 = h1 * width
			print(w2, h2, width + w2, height + h2)
			c = im.crop((w2, h2, width + w2, height + h2))
			buff.append(c)
	return buff



if __name__ == '__main__':
	# 画像の読み込み
	im = Image.open('qr.png')
	for idx,ig in enumerate(ImgSplit(im)):
		# 保存先フォルダの指定
		ig.save(str(idx+1)+".png", "PNG")

