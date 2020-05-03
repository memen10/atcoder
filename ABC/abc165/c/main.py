import sys
input = lambda: sys.stdin.readline().strip()

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np
import itertools

def main():
    N, M, Q = map(int, readline().split())

    A = np.array(list(itertools.combinations_with_replacement(range(1, M + 1), N)))

    n = len(A)
    score = np.zeros(n, np.int32)
    m = map(int, read().split())
    for a, b, c, d in zip(m, m, m, m):
        cond = A[:, b - 1] - A[:, a - 1] == c
        score += d * cond

    print(score.max())

main()
