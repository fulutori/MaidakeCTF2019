import random

def get_text():
	# 問題文の読み込み
	with open('org.txt', 'r') as f:
		flag_text = f.readlines()

		# 問題文の整形
		for i in range(len(flag_text)):
			flag_text[i] = flag_text[i].replace('\n', '')

	return flag_text

def key():
	# 英小文字の置換表の作成
	from_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	while True:
		# 変換予定のリストを作成
		to_list = random.sample(from_list, len(from_list))
		flag = True
		key = {}

		for idx, moji in enumerate(from_list):
			# 置換しても文字が同じときはやり直し
			if moji == to_list[idx]:
				flag = False
				break

			# ちゃんと文字が変わるときはそれで辞書を作成
			else:
				key[moji] = to_list[idx]

		if flag == True:
			break

	return key

def encrypt(plain, key):
	cipher = ''
	for sentence in plain:
		for moji in sentence:
			if moji in key:
				cipher += key[moji]
			else:
				cipher += moji
		cipher += '\n'

	return cipher


if __name__ == '__main__':
	plain = get_text()
	cipher = encrypt(plain, key())

	with open('problem.txt', 'w') as f:
		f.write(cipher)
