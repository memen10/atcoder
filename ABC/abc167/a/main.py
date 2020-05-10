import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().strip()

def main():
    S = input()
    T = input()
    print("Yes" if (1<=len(S) and len(S)<=10) and (T[0:-1]==S) else "No")

main()
