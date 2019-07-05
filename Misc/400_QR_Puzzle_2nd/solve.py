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
		# 確定しているところは辞書に格納
		if puzzle_path == 'r1c1.png':
			puzzle_dic['r1c1'] = cv2.imread(path + puzzle_path)
		elif puzzle_path == 'r1c2.png':
			puzzle_dic['r1c2'] = cv2.imread(path + puzzle_path)
		elif puzzle_path == 'r1c3.png':
			puzzle_dic['r1c3'] = cv2.imread(path + puzzle_path)
		elif puzzle_path == 'r1c4.png':
			puzzle_dic['r1c4'] = cv2.imread(path + puzzle_path)
		elif puzzle_path == 'r2c1.png':
			puzzle_dic['r2c1'] = cv2.imread(path + puzzle_path)
		elif puzzle_path == 'r2c4.png':
			puzzle_dic['r2c4'] = cv2.imread(path + puzzle_path)
		elif puzzle_path == 'r3c1.png':
			puzzle_dic['r3c1'] = cv2.imread(path + puzzle_path)
		elif puzzle_path == 'r3c4.png':
			puzzle_dic['r3c4'] = cv2.imread(path + puzzle_path)
		elif puzzle_path == 'r4c1.png':
			puzzle_dic['r4c1'] = cv2.imread(path + puzzle_path)
		elif puzzle_path == 'r3c2.png':
			puzzle_dic['r4c2'] = cv2.imread(path + puzzle_path)
		elif puzzle_path == 'r1c3.png':
			puzzle_dic['r4c3'] = cv2.imread(path + puzzle_path)
		elif puzzle_path == 'r4c4.png':
			puzzle_dic['r4c4'] = cv2.imread(path + puzzle_path)

		# 確定していない部分は画像名で辞書に格納
		else:
			puzzle_dic[puzzle_path.replace('.png', '')] = cv2.imread(path + puzzle_path)

	return puzzle_dic


# 分割された画像を連結して1つのQRコードを生成
def make_qr(puzzle_dic, puzzle):
	im_list = []
	temp = []

	# 生成された組み合わせでリストを作成
	for idx, im in enumerate(puzzle):
		temp.append(puzzle_dic[im])
		if len(temp) == 4:
			im_list.append(temp)
			temp = []

	# 画像を連結して保存
	im_tile = cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list])
	cv2.imwrite('flag.png', im_tile)

	return im_tile


# 生成されたQRコードを読み取る
def get_qr(qr_code):
	# QRコードの画像をバイナリで開く
	with open('flag.png', 'rb') as f:
		data = f.read()
	image= Image.open(io.BytesIO(data))

	# QRコード読み取り
	result= zbarlight.scan_codes('qrcode', image)

	# 何か文字が出てきたらそれを返す
	if result != None:
		return result[0].decode()
	else:
		return 'None'


if __name__ == '__main__':
	puzzle_dic = read_puzzle()

	# 場所が不明なパズルの一覧
	puzzle_list = ['1', '2', '3', '4']

	# 不明なパズルを総当り
	for pattern in itertools.permutations(puzzle_list):
		puzzle = [ 'r1c1', 'r1c2', 'r1c3', 'r1c4',
					'r2c1',		 0,		 0, 'r2c4',
					'r3c1', 	 0,		 0, 'r3c4',
					'r4c1', 'r4c2', 'r4c3', 'r4c4']
		
		cnt = 0
		for i in range(len(puzzle)):
			if puzzle[i] == 0:
				puzzle[i] = pattern[cnt]
				cnt += 1
				if cnt == len(puzzle_list):
					break

		qr_code = make_qr(puzzle_dic, puzzle)
		flag = get_qr(qr_code)

		# Flagが出てきたら終了
		if 'MaidakeCTF' in flag:
			print(flag)
			break
