import numpy as np


def rotate90_counterclockwise(matrix):
    for i in range(len(matrix) // 2):
        for j in range(len(matrix)):
            tmp = matrix[j][i]
            matrix[j][i] = matrix[j][len(matrix) - i - 1]
            matrix[j][len(matrix) - i - 1] = tmp
    for i in range(1, len(matrix)):
        for j in range(i):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp
    return matrix


def rotate90_clockwise(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp


# determine wether the block can fit into the board in a single direction
def is_fit(board, block):
    for x in range(board.shape[0]):
        for y in range(board.shape[0]):
            if block[x][y] == 1:
                if board[x][y] == 0:
                    continue
                else:
                    return False
    return True


def put_fit(board, block, block_id):
    for x in range(len(block)):
        for y in range(len(block[0])):
            if block[x][y] == 1:
                board[x][y] = block_id


def unput_fit(board, block):
    for x in range(len(block)):
        for y in range(len(block[0])):
            if block[x][y] == 1:
                board[x][y] = 0




def dfs(board, block_id):
    if block_id == len(blocks)+1:
        return True
    block = blocks[block_id - 1]
    N = len(block)
    for x in range(len(board) - N + 1):
        for y in range(len(board) - N + 1):
            block = blocks[block_id - 1]
            r = 0
            while r < 4:
                if is_fit(board[x:x + N, y:y + N], block):
                    put_fit(board[x:x + N, y:y + N], block, block_id)

                    if dfs(board, block_id + 1):
                        return True
                    else:
                        unput_fit(board[x:x + N, y:y + N], block)
                        block = rotate90_counterclockwise(block)
                        r += 1
                else:
                    block = rotate90_counterclockwise(block)
                    r += 1
    return False

board = np.zeros((3, 3))
# holes = [[2, 0]]
# holes = [[0, 0]]
# holes = [[0, 1]]
holes = [[0, 2]]
blocks = [[[1, 0],  # 0
           [1, 0]],
          [[1, 1],  # 1
           [1, 0]],
          [[1, 1],  # 2
           [1, 0]]]


for i in range(len(holes)):
    board[holes[i][0]][holes[i][1]] = -1

print(dfs(board,1))
print(board)