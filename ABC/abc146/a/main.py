import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    S = _S()
    youbi = ["MON","TUE","WED","THU","FRI","SAT","SUN"][::-1]
    print(youbi.index(S) if S!="SUN" else 7)

main()

