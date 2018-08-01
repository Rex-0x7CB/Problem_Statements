def read_matrix():
    matrix = []
    f = open("matrix.txt", "r")
    content = f.readlines()
    for line in content:
        line = line.strip()
        matrix.append(line)

    row = len(matrix)
    col = len(matrix[0])
    print("The game matrix :")
    for i in range(0,row):
        for j in range(0,col):
            print(matrix[i][j],end="")
        print("\n",end="")
    return matrix

def find_popoye(matrix):
    row = len(matrix)
    col = len(matrix[0])
    for i in range(0, row):
        for j in range(0,col):
            if matrix[i][j] == "P":
                print("Popoye found at {},{}".format(i, j))
                return i, j


def met_olive(matrix, y, x):
    try:
        if x-1 < 0:
            raise AccessError
        if matrix[y][x-1] == "O":
            return True
    except:
        print("", end="")

    try:
        if matrix[y][x+1] == "O":
            return True
    except:
        print("", end="")

    try:
        if y-1 < 0:
            raise AccessError
        if matrix[y-1][x] == "O":
            return True
    except:
        print("", end="")

    try:
        if matrix[y+1][x] == "O":
            return True
    except:
        print("", end="")

    return False


def check_move(matrix, y, x):
    available_moves = []
    try:
        if x-1 < 0:
            raise AccessError
        if matrix[y][x-1] == ".":
            available_moves.append("L")
    except:
        print("", end="")

    try:
        if matrix[y][x+1] == ".":
            available_moves.append("R")
    except:
        print("", end="")

    try:
        if y-1 < 0:
            raise AccessError
        if matrix[y-1][x] == ".":
            available_moves.append("U")
    except:
        print("", end="")

    try:
        if matrix[y+1][x] == ".":
            available_moves.append("D")
    except:
        print("", end="")

    return available_moves


def shift(matrix, y, x, direction):

    row = len(matrix)
    col = len(matrix[0])

    new_matrix = matrix[::]

    temp = list(matrix[y])
    temp[x] = "*"
    new_matrix[y] = "".join(temp)

    if direction == "L":
        temp = list(new_matrix[y])
        temp[x-1] = "P"
        new_matrix[y] = "".join(temp)

    if direction == "R":
        temp = list(new_matrix[y])
        temp[x+1] = "P"
        new_matrix[y] = "".join(temp)

    if direction == "U":
        temp = list(new_matrix[y-1])
        temp[x] = "P"
        new_matrix[y-1] = "".join(temp)

    if direction == "D":
        temp = list(new_matrix[y+1])
        temp[x] = "P"
        new_matrix[y+1] = "".join(temp)

    for i in range(0,row):
        for j in range(0,col):
            print(new_matrix[i][j], end="")
        print("\n", end="")
    print("\n",end="")
    return new_matrix

def move(matrix, y, x):
    print("Current Position = ({},{})".format(y, x))
    if met_olive(matrix, y, x) == True:
        print("Popeye Found Olive.\nPopoye <3 Olive")
        exit()
    else:
        moves = check_move(matrix, y, x)
        if len(moves) == 0:
            print("Backtracking...")
        for direction in moves:
            if direction == "L":
                print("Moving Left")
                new_matrix = shift(matrix, y, x, direction)
                move(new_matrix, y, x-1)
            if direction == "R":
                print("Moving Right")
                new_matrix = shift(matrix, y, x, direction)
                move(new_matrix, y, x+1)
            if direction == "U":
                print("Moving Up")
                new_matrix = shift(matrix, y, x, direction)
                move(new_matrix, y-1, x)
            if direction == "D":
                print("Moving Down")
                new_matrix = shift(matrix, y, x, direction)
                move(new_matrix, y+1, x)


def main():
    print("Scanning Game Matrix...")
    matrix = read_matrix()
    print("\n\nLocating Popoye...")
    y, x = find_popoye(matrix)
    move(matrix, y, x)
if __name__ == '__main__':
    main()
