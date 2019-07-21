import socket

host = 'localhost'
port = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# 最初の「What is this MD5?」が邪魔なので予め取得しておく
client.recv(4096).decode().split()

def get_md5():
	md5_dic = {}
	with open('md5_list.csv', 'r') as f:
		md5_list = [line.replace('\n','').split(',') for line in f.readlines()]

	for md5 in md5_list:
		md5_dic[md5[1]] = md5[0]

	return md5_dic


if __name__ == '__main__':
	md5_dic = get_md5()
	
	while True:
		res = client.recv(4096).decode()

		# Flagが無いときはMD5の検索結果を送信
		if not 'MaidakeCTF' in res:
			md5 = res.split()[0]
			if md5 in md5_dic:
				client.send(md5_dic[md5].encode())
		else:
			print(res)
			break
