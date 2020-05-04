import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().strip()

def main():
    N, Y = map(int,input().split())

    for a in range(N+1):
        for b in range(N+1):
            if N-a-b>=0:
                c = N-a-b
            else:
                break
            if 10000*a+5000*b+1000*c == Y:
                print(a,b,c);exit()
    print(-1,-1,-1)

main()