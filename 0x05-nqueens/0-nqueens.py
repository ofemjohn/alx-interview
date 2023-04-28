#!/usr/bin/python3
'''interview for chesse queen'''
import sys


def nqueens(n):
    '''return ueens'''
    def save_nqueen(board, row, col):
        '''save queen'''
        for i in range(col):
            if board[i] == row or \
               board[i] - i == row - col or \
               board[i] + i == row + col:
                return False
        return True

    def solution(board, col, solutions):
        '''find the solution'''
        if col == n:
            solutions.append(board[:])
            return

        for row in range(n):
            if save_nqueen(board, row, col):
                board[col] = row
                solution(board, col + 1, solutions)
                board[col] = -1

    board = [-1] * n
    solutions = []
    solution(board, 0, solutions)

    for s in solutions:
        print([[i, s[i]] for i in range(n)])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

nqueens(n)
