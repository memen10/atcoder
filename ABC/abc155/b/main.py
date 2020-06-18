import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    N = I()
    A = numpy.array(LI())
    A_mod2 = A[A%2==0]
    is_approved = ((A_mod2%3==0)|(A_mod2%5==0)).all(axis=0)
    print("APPROVED" if is_approved else "DENIED")

main()

