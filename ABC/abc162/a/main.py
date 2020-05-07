import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().strip()

def main():
    N = input()
    print("Yes" if '7' in N else "No")

main()
