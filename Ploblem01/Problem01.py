# Solution Developed By Prashant Gupta

def boundary_sum(matrix, offset_row, offset_col, row, col):
	sum = 0
	for i in range(0+offset_row, row+offset_row):
		for j in range(0+offset_col, col+offset_col):
			if i==0+offset_row or j==0+offset_col or i==row+offset_row-1 or j==col+offset_col-1:
				sum = sum + int(matrix[i][j])
	return sum

def print_boundary(matrix, offset_row, offset_col, row, col):
	for i in range(0+offset_row, row+offset_row):
		for j in range(0+offset_col, col+offset_col):
			print(matrix[i][j],end=" ")
		print("")


def get_input(row, col):
	matrix = []
	for i in range(0, row):
		temp = input()
		temp = list(temp.split(" "))
		matrix.append(temp)

	return matrix


def main():
	print("Enter the number of columns:", end=" ")
	col = int(input())
	print("Enter the number of rows:", end=" ")
	row = int(input())
	matrix = get_input(row, col)

	print("Input maximum width of square submatrix (for square submatrix height and width are same) :", end = "")
	side = int(input())
	
	print("\n")

	maxim = 0
	max_index = (0,0)
	for i in range(0, row-side+1):
		for j in range(0, col-side+1):
			temp = boundary_sum(matrix, i, j, side, side)
		if temp > maxim:
			maxim = temp
			max_index = (i,j)

	print_boundary(matrix, max_index[0], max_index[1], side, side)


if __name__ == '__main__':
	main()