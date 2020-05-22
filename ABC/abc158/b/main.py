import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    N,A,B = LI()
    ans = 0
    n_ab = int(N/(A+B))
    amari = N-n_ab*(A+B)
    ans = n_ab*A+A if amari >= A else n_ab*A+amari
    print(ans)

main()

