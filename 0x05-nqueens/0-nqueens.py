#!/usr/bin/env python3
'''
programm that places N non-attacking
queens on an NxN chessboard
'''
import sys

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)
if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)
if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)
n = int(sys.argv[1])


def nqueens(N, x=0, a=[], b=[], c=[]):
    '''return queens'''
    if x < N:
        for j in range(N):
            if j not in a and x + j not in b and x - j not in c:
                yield from nqueens(N, x + 1, a + [j], b + [x + j], c + [x - j])
    else:
        yield a


def solution(n):
    '''append nqueens'''
    q = []
    i = 0
    for solution in nqueens(n, 0):
        for sol in solution:
            q.append([i, sol])
            i += 1
        print(q)
        k = []
        i = 0


solution(n)
