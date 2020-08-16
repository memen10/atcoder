import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    N = I()
    L = LI()
    l_comb = list(set(itertools.combinations(L,3)))

    ans = 0
    for l in l_comb:
        if l[0]+l[1]>l[2] and l[1]+l[2]>l[0] and l[2]+l[0]>l[1]:
            ans += 1
            print(l)
    print(ans)

main()

