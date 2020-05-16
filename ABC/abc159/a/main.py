import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    N,M = LI()
    even_num = N*(N-1)/2    #NC2
    odd_num = M*(M-1)/2     #MC2
    print(int(even_num + odd_num))

main()
