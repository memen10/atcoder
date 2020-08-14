import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    N,K,M = LI()
    A = LI()
    N_req = (N*M - sum(A)) if (N*M - sum(A))>0 else 0
    print(N_req if N_req<=K else -1)

main()

