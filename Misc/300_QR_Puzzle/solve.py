import itertools
puzzle_list = [1, 2, 3, 4, 5]

for pattern in itertools.permutations(puzzle_list):
	puzzle = ['lu', 0, 'ru', 0, 0, 0, 'ld', 0, 'rd']
	
	cnt = 0
	for i in range(len(puzzle)):
		if puzzle[i] == 0:
			puzzle[i] = pattern[cnt]
			cnt += 1
			if cnt == len(puzzle_list):
				break

	print(puzzle)