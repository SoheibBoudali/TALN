filename  = 'test.txt'

with open(filename, 'r') as f:
	lines = f.readlines()
	for l in reversed(lines):
		print(l)