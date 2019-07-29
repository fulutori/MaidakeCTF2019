import sys

sys.setrecursionlimit(100000)
def fib(n):
	if n <= 1:
		return n
	return fib(n-1) + fib(n-2)

in_flag = str(fib(8192))[:40]
print ("MaidakeCTF{"+in_flag+"}")