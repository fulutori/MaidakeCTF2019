from PIL import Image
import urllib.request
import cv2
import os
import io
import zbarlight

base_url = "http://maidakectf2019.aokakes.work/problems/http/QR_Puzzle_Final/"
p_list = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png"]

md5 = "4910b4bb34215367afd5e281954b1f6d"

def download(md5):
	if not os.path.exists(md5):
		os.makedirs("puzzle/{}".format(md5))
	for p in p_list:
		urllib.request.urlretrieve("{}/{}/puzzle/{}".format(base_url, md5, p), "puzzle/{}/{}".format(md5, p))


def read_puzzle(md5):
	path = "puzzle/{}".format(md5)
	puzzle = []
	puzzles_path = sorted(os.listdir(path))
	
	for puzzle_path in puzzles_path:
		puzzle.append(cv2.imread('{}/{}'.format(path, puzzle_path)))

	return puzzle


def make_qr(puzzle):
	im_list = []
	temp = []
	cnt = 0
	for i in range(9):
		temp.append(puzzle[i])
		if len(temp) == 3:
			im_list.append(temp)
			temp = []

	im_tile = cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list])
	cv2.imwrite('tile.png', im_tile)

	return im_tile


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
	cnt = 1
	while True:
		download(md5)
		puzzle = read_puzzle(md5)
		qr_code = make_qr(puzzle)

		md5 = get_qr(qr_code)
		print('{} : {}'.format(cnt, md5))
	
		if 'MaidakeCTF' in md5:
			break
		else:
			cnt += 1