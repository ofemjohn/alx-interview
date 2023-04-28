#!/usr/bin/python3
'''chesse queen algorithm'''
import sys


class nqueen:
    '''nqueen class'''
    def __init__(self, N):
        '''init'''
        self.N = N
        self.x = [0 for i in range(N + 1)]
        self.res = []

    def place_chess(self, k, i):
        ''''checks if n has been placed'''
        for j in range(1, k):
            if self.x[j] == i or \
               abs(self.x[j] - i) == abs(j - k):
                return 0
        return 1

    def nqueens(self, k):
        '''placing queen'''
        for i in range(1, self.N + 1):
            if self.place_chess(k, i):
                self.x[k] = i
                if k == self.N:
                    solution = []
                    for i in range(1, self.N + 1):
                        solution.append([i - 1, self.x[i] - 1])
                    self.res.append(solution)
                else:
                    self.nqueens(k + 1)
        return self.res


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

n = sys.argv[1]

try:
    n = int(n)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = nqueen(n)
res = queen.nqueens(1)

for i in res:
    print(i)
