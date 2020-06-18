import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    N = I()
    S = [_S() for _ in range(N)]
    S_count = collections.Counter(S).most_common()
    S_most = list(filter(lambda t:t[1]>=S_count[0][1],S_count))
    for s in sorted(S_most,key=lambda tup:tup[0]):
        print(s[0])

main()

