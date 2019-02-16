#!/usr/bin/env python
# coding: utf-8

# # DFS version

# In[1]:


import numpy as np
# one way to do the rotation
def rotate90_counterclockwise(matrix):
    for i in range(len(matrix)//2):
        for j in range(len(matrix)):
            tmp = matrix[j][i]
            matrix[j][i] = matrix[j][len(matrix)-i-1]
            matrix[j][len(matrix)-i-1] = tmp
    for i in range(1,len(matrix)):
        for j in range(i):
            tmp=matrix[i][j]
            matrix[i][j]=matrix[j][i]
            matrix[j][i]=tmp
    return matrix
# Just another way to do rotation
def rotate90_clockwise(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp

# board is a part of board
# block is of the same size of board
# Example: board = [[ 0,0],
#                   [-1,0]]
#          block = [[0,0],
#                   [1,1]]
# For blocks 1 represent a block, 0 represent emptiness
# For board -1 means the hole, 1~9 means the square of blocks, 0 means empty
# Test wether a piece can fit into certain part of board
# Board and block have to be same size and both square
def is_fit(board, block):
    for x in range(board.shape[0]):
        for y in range(board.shape[0]):
            if block[x][y] == 1:
                if board[x][y] == 0:
                    continue
                else:
                    return False
    return True

# put one piece on board
def put_fit(board, block, block_id):
    for x in range(len(block)):
        for y in range(len(block[0])):
            if block[x][y] == 1:
                board[x][y] = block_id

# remove one piece on board
def unput_fit(board, block):
    for x in range(len(block)):
        for y in range(len(block[0])):
            if block[x][y] == 1:
                board[x][y] = 0

# Rotate the block four times and try to fit it into board
# It's not a good solution to use just dfs
def solution(board, holes, blocks):
    def dfs(board, block_id):
        if block_id == len(blocks)+1:
            return True
        block = blocks[block_id - 1]
        N = len(block)
        # Move the window of block to every position of board and try to fit in
        for x in range(len(board) - N + 1):
            for y in range(len(board) - N + 1):
                block = blocks[block_id - 1]
                r = 0
                while r < 4: # four direction
                    if is_fit(board[x:x + N, y:y + N], block):
                        put_fit(board[x:x + N, y:y + N], block, block_id)
                        # Just try get one solution first
                        if dfs(board, block_id + 1):
                            return True
                        else:
                            # failed, remove the block from board
                            unput_fit(board[x:x + N, y:y + N], block)
                            block = rotate90_counterclockwise(block)
                            r += 1
                    else:
                        block = rotate90_counterclockwise(block)
                        r += 1
        return False

    board_tmp = board.copy()
    # for each hole on the board
    for i in range(len(holes)):
        board = board_tmp.copy()
        board[holes[i][0]][holes[i][1]] = -1
        print(dfs(board,1))
        print(board)


# # Test

# In[ ]:


board = np.zeros((3,3))
holes = [[2,0],[0,0],[0,1],[0,2]]
blocks = [[[1,0],  #0
           [1,0]],
          [[1,1],  #1
           [1,0]],
          [[1,1],  #2
           [1,0]]
         ]
solution(board,holes,blocks)


# # Todo & Thoughts
#
# 1. Add isolated 0 detaction to trim the search tree
# 1. Add a heuristic and try A* instead of DFS
