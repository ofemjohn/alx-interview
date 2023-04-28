#!/usr/bin/env python3
'''
programm that places N non-attacking
queens on an N×N chessboard
'''
import sys


def nqueens(N):
    '''the nqueen function'''
    if not isinstance(N, int):
        print('N must be a number')
        sys.exit(1)
    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

    def save_nqueen(board, row, col):
        '''returning non attacking queens'''
        for i in range(row):
            if board[i] == col or \
                    board[i] - i == col - row or \
                    board[i] + i == col + row:
                return False
        return True

    def solve(board, row, solutions):
        '''appending the save nqueen into the board'''
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if save_nqueen(board, row, col):
                board[row] = col
                solve(board, row + 1, solutions)

    board = [0] * N
    solutions = []
    solve(board, 0, solutions)
    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

nqueens(N)
