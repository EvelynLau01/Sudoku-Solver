board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(bo):

    find = find_empty(bo) # Call the function to get an empty pos

    # if there's no empty space, we had already solved the sudoku
    if not find:
        return True

    else:
        row, col = find

    # try the empty spot with digit from 1 to 9
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            # if valid, then add it to the board
            bo[row][col] = i

            # run recursively to solve the remaining board until
            # not empty spot left
            if solve(bo):
                return True

            # set to empty if non-valid, try it with different digit
            bo[row][col] = 0

    return False

def valid(bo, num, pos):
    """
    :param bo: board
    :param num: digit to be checked
    :param pos: empty position - (row, col)
    :return:
    """

#     Check row
    for i in range(len(bo[0])):
        # Check that row and make sure we're not checking
        # the exact position of the number itself
        # pos[0] corresponds to the row of the num
        # pos[1] corresponds to the col of the num
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

#     Check col
    for i in range(len(bo[0])):
        # Check that col and make sure we're not checking
        # the exact position of the number itself
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

#     Check box - 3x3
    box_x = pos[1] // 3 # give either 0, 1 or 2
    box_y = pos[0] // 3

    # loop through that particular box
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True



def print_board(bo):

    for i in range(len(bo)):

        # To print a line after every 3 rows
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        for j in range(len(bo[0])):

            # To print a | for after printing every number
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            # To print each numbers, newline for the last number
            # of each row
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

# print_board(board)

def find_empty(bo):

    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j] == 0:
                return (i, j) # return empty row, col
    return None


if __name__ == "__main__":
    print_board(board)
    solve(board)

    print("Solved Board")
    print("_______________________")
    print_board(board)