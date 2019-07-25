import socket

host = 'localhost'
port = 15410

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# 余計な文字は予め取得しておく
client.recv(35).decode()

def calc(problem):
	if problem[1] == '+':
		return str(int(problem[0]) + int(problem[2]))
	elif problem[1] == '-':
		return str(int(problem[0]) - int(problem[2]))
	

if __name__ == '__main__':

	while True:
		res = client.recv(1024).decode()
		print(res)

		if not 'MaidakeCTF' in res:
			problem = res.split()
			ans = calc(problem)
			print(ans)
			client.send(ans.encode())
		else:
			break
