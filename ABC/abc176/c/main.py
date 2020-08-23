import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    N = I()
    A = LI()
    a_max = A[0]
    ans = 0
    for i in range(1,len(A)):
        if A[i]<a_max:
            ans += a_max-A[i]
        else:
            a_max = A[i]
    print(ans)

main()

