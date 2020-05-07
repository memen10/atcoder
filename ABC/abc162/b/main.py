import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().strip()

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        if not(i%3==0 or i%5==0):
            ans += i
    print(ans)
main()
