import itertools
import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().strip()

"""
[WIP]
"""
def main():
    N = int(input())
    S = input()
    ijk_list = list(itertools.combinations([i for i in range(1,N+1)],3))
    ans = 0
    for i,j,k in ijk_list:
        i,j,k = i-1,j-1,k-1
        if (S[i]!=S[j] and S[j]!=S[k] and S[k]!=S[i]) and (j-i)!=(k-j):
            ans += 1
    print(ans)

main()
