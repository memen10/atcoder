import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())


def digitSum(n):
    s = str(n)
    array = list(map(int, s))
    return sum(array)

def main():
    N = I()
    dig_sum = digitSum(N)
    print("Yes" if dig_sum%9==0 else "No")

main()

