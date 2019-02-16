import numpy as np


class State:
    # class variables of the puzzle
    holes = None
    blocks = None

    # block_id represent all blocks before the id have been placed on board
    def __init__(self, board=None, block_id=0):
        self.board = board
        self.block_id = block_id

    def put_hole(self, hole_id):
        self.board[State.holes[hole_id][0]][State.holes[hole_id][1]] = -1

    # staic method
    def is_fit(board, block):
        for x in range(board.shape[0]):
            for y in range(board.shape[0]):
                if block[x][y] == 1:
                    if board[x][y] == 0:
                        continue
                    else:
                        return False
        return True

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

    # put one piece on board
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

    # return a list of possible state from current state
    # return True if all blocks have been put on the board
    # puts next blocks on the board
    def next_level(self):
        self.block_id += 1
        board_list = []
        if self.block_id == len(State.blocks) + 1:
            return True
        block = State.blocks[self.block_id - 1]
        N = len(block)
        for x in range(len(self.board) - N + 1):
            for y in range(len(self.board) - N + 1):
                block = State.blocks[self.block_id - 1]
                r = 0
                while r < 4:  # four direction
                    if State.is_fit(self.board[x:x + N, y:y + N], block):
                        State.put_fit(self.board[x:x + N, y:y + N], block, self.block_id)
                        board_list.append(self.board.copy())
                        State.unput_fit(self.board[x:x + N, y:y + N], block)
                        block = State.rotate90_counterclockwise(block)
                        r += 1
                    else:
                        block = State.rotate90_counterclockwise(block)
                        r += 1
        return board_list



State.holes = [[3,0]]
State.blocks =   [[[1,1],  #0
                   [1,0]],
                  [[1,1,0],
                   [0,1,1],
                   [0,0,1]],
                  [[1,0,0],
                   [1,1,0],
                   [0,1,0]],
                  [[1,1],  #2
                   [1,0]]]
s1 = State(np.zeros((4,4)),0)
s1.put_hole(0)
list = s1.next_level()

for i in range(5):
    print(list[i])

len(list)