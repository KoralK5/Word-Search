from matplotlib import pyplot as plt

def search(puzzle, word, row, col):
	l = len(word)
	
	try:
		right = ''.join(puzzle[row][col:col+l])
	except:
		right = ''

	try:
		left = ''.join(puzzle[row][col-l:col][::-1])
	except:
		left = ''

	letters = [right, left, '', '', '', '', '', '']
	directions = [(row, col+l), (row, col-l), (row-l, col), (row+l, col), (row-l, col+l), (row+l, col+l), (row-l, col-l), (row+l, col-l)]
	for x in range(l):
		try:
			letters[2] += puzzle[row-x][col]
		except:
			letters[2] = ''

		try:
			letters[3] += puzzle[row+x][col]
		except:
			letters[3] = ''
		
		try:
			letters[4] += puzzle[row-x][col+x]
		except:
			letters[4] = ''

		try:
			letters[5] += puzzle[row+x][col+x]
		except:
			letters[5] = ''
		
		try:
			letters[6] += puzzle[row-x][col-x]
		except:
			letters[6] = ''

		try:
			letters[7] += puzzle[row+x][col-x]
		except:
			letters[7] = ''
	
	if word in letters:
		return True, directions[letters.index(word)]

	return False, 0

def plot(loc):
	for row in loc:
		plt.plot((row[1][1], row[2][1]), (len(puzzle)-row[1][0], len(puzzle)-row[2][0]), alpha=0.7, linewidth=10, label=row[0])

	plt.title('Word Search')
	plt.xlabel('Row')
	plt.ylabel('Column')
	
	plt.legend()
	plt.show()

puzzle, words = open('wordSearch.txt').read().split('\n\n')

puzzle = [row.split('\t') for row in puzzle.split('\n')]
words = words.split()

row, col, loc = 0, 0, []
while len(words) != 0:
	for word in words:
		func = search(puzzle, word, row, col)
		if func[0]:
			loc += [[word, (row, col), func[1]]]
			words.remove(word)
	
	row = (row+1)%len(puzzle[0])
	if row%len(puzzle[0]) == 0:
		col += 1

plot(loc)
