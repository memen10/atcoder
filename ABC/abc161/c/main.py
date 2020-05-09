import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().strip()

def main():
    N,K = map(int,input().split())
    ans = N%K
    print(ans if ans<abs(ans-K) else abs(ans-K))

main()
