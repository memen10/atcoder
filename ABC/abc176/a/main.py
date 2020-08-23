import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    N, X, T = LI()
    print(int(int(N/X)*T) if N%X==0 else int(int(N/X+1)*T))

main()

