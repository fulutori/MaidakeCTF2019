
def get_text():
	# 問題文の読み込み
	with open('problem.txt', 'r') as f:
		flag_text = f.readlines()

		# 問題文の整形
		for i in range(len(flag_text)):
			flag_text[i] = flag_text[i].replace('\n', '')

	return flag_text

def moji_count(cipher):
	moji_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	
	frequency = {}
	for sentence in cipher:
		for moji in sentence:
			if moji in moji_list:
				if moji in frequency:
					frequency[moji] += 1
				else:
					frequency[moji] = 1

	return sorted(frequency.items(), key=lambda x: -x[1])

def key(frequency):
	#maybe = ['e', 'i', 'a', 't', 'n', 's', 'o', 'r', 'l', 'd', 'c', 'h', 'u', 'm', 'p', 'f', 'g', 'y', 'w', 'k', 'v', 'b', 'j', 'q', 'x', 'z']
	#maybe = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']
	maybe = ['e', 'a', 't', 'i', 'o', 's', 'n', 'r', 'h', 'l', 'd', 'c', 'u', 'm', 'p', 'f', 'g', 'y', 'w', 'b', 'v', 'k', 'j', 'x', 'q', 'z']
	
	key = {}
	for idx, pair in enumerate(frequency):
		key[pair[0]] = maybe[idx]
	
	key = {
	'a': 'v', 
	'b': 'x', 
	'c': 'a', 
	'd': 's', 
	'e': 'j', 
	'f': 't', 
	'g': 'u', 
	'h': 'o', 
	'i': 'q', 
	'j': 'e', 
	'k': 'g', 
	'l': 'b', 
	'm': 'h', 
	'n': 'w', 
	'o': 'm', 
	'p': 'k', 
	'q': 'z', 
	'r': 'f', 
	's': 'i', 
	't': 'd', 
	'u': 'r', 
	'v': 'p', 
	'w': 'c', 
	'x': 'y', 
	'y': 'n', 
	'z': 'l'}

	return key

def decrypt(cipher, key):
	plain = ''

	for sentence in cipher:
		for moji in sentence:
			if moji in key:
				plain += key[moji]
			else:
				plain += moji
		plain += '\n'

	return plain

if __name__ == '__main__':
	cipher = get_text()
	frequency = moji_count(cipher)
	
	plain = decrypt(cipher, key(frequency))
	
	with open('flag.txt', 'w') as f:
		f.write(plain)