from numpy.random import *
import socketserver
import socket
import sys

HOST, PORT = 'localhost', 17270
FLAG = 'The Flag is MaidakeCTF{Themachine_gives_accurate_answers_even_if_the_calculation_is_complicated}'
q_num = 500

class Handler(socketserver.BaseRequestHandler, object):
	def handle(self):
		client = self.request
		client.send('Please calculate.\nBut division must be truncated to an integer.\n'.encode())

		for i in range(q_num):
			try:
				# 問題の準備
				problem = make_problem()
				#print(problem)

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
			except Exception as e:
				self.request.send('Invalid input.\n'.encode())
				print(e.args)
				return

		self.request.send('\n\nCongratulations!\n{}\n'.format(FLAG).encode())
			

class Server(socketserver.ThreadingTCPServer, object):
	def server_bind(self):
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.socket.bind(self.server_address)

def make_problem():
	sign = choice(['+', '-', '*', '/'], 1)[0]
	x = 0
	y = 0
	while x==0 and y==0:
		x = randint(1000000000)
		y = randint(1000000000)
	formula = '{} {} {}'.format(x, sign, y)

	return make_answer(formula)

def make_answer(formula):
	shiki = formula.split()
	if shiki[1] == '+':
		return [formula, int(shiki[0]) + int(shiki[2])]
	elif shiki[1] == '-':
		return [formula, int(shiki[0]) - int(shiki[2])]
	elif shiki[1] == '*':
		return [formula, int(shiki[0]) * int(shiki[2])]
	elif shiki[1] == '/':
		return [formula, int(shiki[0]) // int(shiki[2])]

if __name__ == "__main__":
	server = Server((HOST, PORT), Handler)
	server.serve_forever()
