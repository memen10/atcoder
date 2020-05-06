import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().strip()

def main():
    N,M = map(int,input().split())
    A_list = list(map(int,input().split()))

    for i in A_list:
        N -= i
    print(N if N>=0 else -1)

main()
