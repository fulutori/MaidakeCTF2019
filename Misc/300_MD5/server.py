from numpy import random as rnd
import socketserver
import socket

HOST, PORT = 'localhost', 12345
FLAG = 'The Flag is MaidakeCTF{CTF_may_hide_hints_for_other_issues}'
q_num = 50

class SampleHandler(socketserver.BaseRequestHandler, object):
	def handle(self):
		client = self.request
		client.send('What is this MD5?\n'.encode())

		# クライアントごとに問題を取得
		md5_list = get_md5()
		#print(md5_list)

		for question in md5_list:
			try:
				# 1問あたりの制限時間は30秒
				client.settimeout(30)

				# クライアントに問題を送信
				print('ans:{} question:{}'.format(question[0], question[1]))
				self.request.send('\n{}\n>>'.format(question[1]).encode())

				# クライアントの答えを取得
				client_ans = client.recv(80).strip().decode()

				# クライアントの答えが不正解のときは終了
				if client_ans != question[0]:
					self.request.send('The answer is wrong.\n'.encode())
					return

			except socket.timeout as e:
				self.request.send('\nTimeout...\n'.encode())
				return
			except socket.error as e:
				self.request.send('\nSorry, connection error...\n')
				return
			except:
				return

		self.request.send('\n\nCongratulations!\n{}\n'.format(FLAG).encode())
			

class SampleServer(socketserver.ThreadingTCPServer, object):
	def server_bind(self):
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.socket.bind(self.server_address)

def get_md5():
	with open('md5_list.csv', 'r') as f:
		md5_list = [line.replace('\n','').split(',') for line in f.readlines()]

	rnd.shuffle(md5_list)
	return md5_list[:q_num]

if __name__ == "__main__":
	server = SampleServer((HOST, PORT), SampleHandler)
	server.serve_forever()

