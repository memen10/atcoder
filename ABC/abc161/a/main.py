import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().strip()

def main():
    X,Y,Z = map(int,input().split())
    print(Z,X,Y)

main()
