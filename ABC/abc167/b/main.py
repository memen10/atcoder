import itertools
import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().strip()

def main():
    A,B,C,K = map(int,input().split())

    a = K if A>=K else A
    b = (K-a) if B>=(K-a) else B
    c = K-a-b if C>=(K-a-b) else C
    print(a-c)


main()
