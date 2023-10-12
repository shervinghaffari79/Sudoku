from math import sqrt

def satisfy_constraint(puzzle , row ,col ,num):
	n = len(puzzle)
	# satisfy column constraint
	for j in range(n):
		if puzzle[row][j] == num:
			return False
	# satisfy row constraint
	for i in range(n):
		if puzzle[i][col] == num:
			return False

	row -= row % int(sqrt(n))
	col -= col % int(sqrt(n))
	# satisfy √n x √n square constraint
	for i in range(int(sqrt(n))):
		for j in range(int(sqrt(n))):
			if puzzle[row+i][col+j] == num:
				return False

	return True

def sudoku(puzzle,row,col):
	# puzzle has been completed successfully
	n = len(puzzle)
	if row == n-1 and col == n:
		return True

	# complete next row
	if col == n:
		row +=1
		col = 0

	# complete next cell
	if puzzle[row][col] > 0:
		return sudoku(puzzle,row,col+1)

	# looking for numbers which can be inserted
	for choice in range(1,n+1):
		# statisfy constraints ?
		if satisfy_constraint(puzzle,row,col,choice):
			puzzle[row][col]=choice
			# our guess is true
			if sudoku(puzzle,row,col+1):
				return True
	# our guess is wrong , we have to reset the value
	puzzle[row][col] = 0

	return False

if __name__ == "__main__":
	n = int(input("n :"))
	c = int(input("c :"))
	puzzle = [[0 for i in range(n)]for j in range(n)]

	for couter in range(c):
		line = input()
		row , col , value = line.split(" ")
		puzzle [int(row)][int(col)] = int(value)

	if sudoku(puzzle,0,0):
		for i in range(n):
			for j in range(n):
				print(puzzle[i][j],end=" ")
			print()
	else:
		print("Unsolvable CSP!")

