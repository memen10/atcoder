import itertools
import sys

import numpy
import numpy as np
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().strip()

def main():
    N,M,X = map(int,input().split())
    # ca_list = np.array([map(int,input().split())] for _ in range(N))
    ca_list = [list(map(int,input().split())) for _ in range(N)]
    nm_comb = []
    for i in range(1,N+1):
        nm_comb.extend(list(itertools.combinations([i for i in range(N)],i)))
    # print(nm_comb)
    ans_list = []
    for selected in nm_comb:
        for i in selected:
            ans_list.append(ca_list[i][1::])
        else:
            numpy.all(ans_list,axis=1)
            ans_list = []
    print(ans_list)
    print(numpy.sum(ans_list,axis=0))


main()
