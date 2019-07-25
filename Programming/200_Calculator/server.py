from numpy.random import *
import socketserver
import socket

HOST, PORT = 'localhost', 15410
FLAG = 'The Flag is MaidakeCTF{It_is_also_possible_to_calculate_it_by_yourself}'
q_num = 50

class Handler(socketserver.BaseRequestHandler, object):
	def handle(self):
		client = self.request
		client.send('Please calculate (All 50 problems).\n'.encode())

		for i in range(q_num):
			try:
				# 問題の準備
				problem = make_problem()

				# 1問あたりの制限時間は30秒
				client.settimeout(10)

				# クライアントに問題を送信
				print('ans:{} problem:{}'.format(problem[1], problem[0]))
				self.request.send('\n{}\n>>'.format(problem[0]).encode())

				# クライアントの答えを取得
				client_ans = int(client.recv(80).strip().decode())
				
				# クライアントの答えが不正解のときは終了
				if client_ans != problem[1]:
					self.request.send('The answer is wrong.\n'.encode())
					return

			except socket.timeout as e:
				self.request.send('\nTimeout...\n'.encode())
				return
			except socket.error as e:
				self.request.send('\nSorry, connection error...\n')
				return
			except:
				self.request.send('Invalid input.\n'.encode())
				return

		self.request.send('\n\nCongratulations!\n{}\n'.format(FLAG).encode())
			

class Server(socketserver.ThreadingTCPServer, object):
	def server_bind(self):
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.socket.bind(self.server_address)

def make_problem():
	sign = choice(['+', '-'], 1)[0]
	x = randint(100)
	y = randint(100)
	formula = '{} {} {}'.format(x, sign, y)

	return make_answer(formula)

def make_answer(formula):
	shiki = formula.split()
	if shiki[1] == '+':
		return [formula, int(shiki[0]) + int(shiki[2])]
	elif shiki[1] == '-':
		return [formula, int(shiki[0]) - int(shiki[2])]

if __name__ == "__main__":
	server = Server((HOST, PORT), Handler)
	server.serve_forever()
