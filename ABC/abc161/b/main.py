import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().strip()

def main():
    N,M = map(int,input().split())
    A_list = sorted(list(map(int,input().split())),reverse=True)
    print("Yes" if A_list[M-1]>=sum(A_list)*(1/(4*M)) else "No")

main()
