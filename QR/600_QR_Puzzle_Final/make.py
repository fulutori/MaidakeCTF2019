from PIL import Image
import qrcode
import hashlib
import os

flag = "MaidakeCTF{I_don't_know_why_I_made_many_QR_code_problem}"

img = qrcode.make(flag)
img = img.resize((330, 330))
img.save('flag.png')
#md5 = hashlib.md5(flag).hexdigest()
md5 = flag

def ImgSplit(img):
	height = 110
	width = 110

	buff = []
	# 縦の分割枚数
	for h1 in range(3):
		# 横の分割枚数
		for w1 in range(3):
			w2 = w1 * height
			h2 = h1 * width
			#print(w2, h2, width + w2, height + h2)
			c = img.crop((w2, h2, width + w2, height + h2))
			buff.append(c)
	return buff


if __name__ == '__main__':
	for i in range(50):

		md5 = hashlib.md5(md5.encode('unicode-escape')).hexdigest()
		md5_2 = hashlib.md5(md5.encode('unicode-escape')).hexdigest()

		# QRコードごとにディレクトリを作成
		dir_path = "./temp/{}/puzzle/".format(md5)
		print(dir_path)
		if not os.path.exists(dir_path):
			os.makedirs(dir_path)


		# 9分割したQRコードを保存
		for idx,ig in enumerate(ImgSplit(img)):
			ig.save("{}{}.png".format(dir_path, idx+1), "PNG")

		dir_path = "./temp/{}/puzzle/".format(md5_2)
		os.makedirs(dir_path)
		img = qrcode.make(md5).resize((330, 330))
		img.save('{}qr.png'.format(dir_path))


