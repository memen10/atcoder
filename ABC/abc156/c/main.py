import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    N = I()
    X = LI()
    energy = [0 for _ in range(1,100)]
    for p in range(1,100):
        for x in X:
            energy[p-1] += (x-p)**2
    print(min(energy))

main()

