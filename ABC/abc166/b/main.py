import itertools
import sys
import numpy as np
input = lambda: sys.stdin.readline().strip()

def main():
    N,K = map(int,input().split())
    itadura = list()
    sunuke_list = [i for i in range(1,N+1)]
    A = list()
    for _ in range(N):
        d = input()
        A.append(map(int,input().split()))
    for ls in A:
        for j in ls:
            itadura.append(j)
    ans = set(sunuke_list) - set(itadura)
    print(len(ans))




main()
