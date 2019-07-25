from PIL import Image
import numpy as np
import itertools
import os
import cv2
import io
import zbarlight

# 画像読み込み
def read_puzzle():
	path = 'puzzle/'
	puzzle_dic = {}
	puzzles_path = os.listdir(path)

	for puzzle_path in puzzles_path:
		# 四隅は変数で保存
		if puzzle_path == 'lu.png':
			puzzle_dic['lu'] = cv2.imread(path + puzzle_path)
		elif puzzle_path == 'ru.png':
			puzzle_dic['ru'] = cv2.imread(path + puzzle_path)
		elif puzzle_path == 'ld.png':
			puzzle_dic['ld'] = cv2.imread(path + puzzle_path)
		elif puzzle_path == 'rd.png':
			puzzle_dic['rd'] = cv2.imread(path + puzzle_path)

		# 四隅以外はリストにまとめて保存
		else:
			puzzle_dic[puzzle_path.replace('.png', '')] = cv2.imread(path + puzzle_path)

	return puzzle_dic

# 分割された画像を連結して1つのQRコードを生成
def make_qr(puzzle_dic, puzzle):
	im_list = []
	temp = []
	cnt = 0
	for idx, im in enumerate(puzzle):
		temp.append(puzzle_dic[im])
		if len(temp) == 3:
			im_list.append(temp)
			temp = []

	im_tile = cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list])
	cv2.imwrite('tile.png', im_tile)

	return im_tile

# 生成されたQRコードを読み取る
def get_qr(qr_code):
	with open('tile.png', 'rb') as f:
		data = f.read()
	image= Image.open(io.BytesIO(data))
	result= zbarlight.scan_codes('qrcode', image)
	if result != None:
		return result[0].decode()
	else:
		return 'None'

if __name__ == '__main__':
	puzzle_dic = read_puzzle()
	puzzle_list = ['1', '2', '3', '4', '5']

	for pattern in itertools.permutations(puzzle_list):
		puzzle = ['lu', 0, 'ru', 0, 0, 0, 'ld', 0, 'rd']
		
		cnt = 0
		for i in range(len(puzzle)):
			if puzzle[i] == 0:
				puzzle[i] = pattern[cnt]
				cnt += 1
				if cnt == len(puzzle_list):
					break

		qr_code = make_qr(puzzle_dic, puzzle)
		flag = get_qr(qr_code)

		#print(flag)
		if 'MaidakeCTF' in flag:
			print(flag)
			break
