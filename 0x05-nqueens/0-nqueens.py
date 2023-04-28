#!/usr/bin/env python3
'''interview question for chessboard'''
from sys import argv


def save_nqueen(board, row, col):
    '''save n queens'''
    for i in range(row):
        if board[i][col] == 1:
            return False
    (i, j) = (row, col)
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j - 1
    (i, j) = (row, col)
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j + 1
    return True


def queen_sol(board):
    '''return solution'''
    result = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                result.append([i, j])
    print(result)


def nqueen(board, row):
    '''return queen'''
    if row == len(board):
        queen_sol(board)
        return
    for i in range(len(board)):
        if save_nqueen(board, row, i):
            board[row][i] = 1
            nqueen(board, row + 1)
            board[row][i] = 0


if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)
try:
    n = int(argv[1])
except ValueError:
    print('N must be a number')
    exit(1)
if n < 4:
    print('N must be at least 4')
    exit(1)

board = [[0 for x in range(n)] for y in range(n)]
nqueen(board, 0)
