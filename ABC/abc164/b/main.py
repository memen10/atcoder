import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().strip()

def main():
    A,B,C,D = map(int,input().split())
    takahashi_num = int(C/B) if C%B==0 else int(C/B)+1
    aoki_num = int(A/D) if A%D==0 else int(A/D)+1
    print("Yes" if takahashi_num<=aoki_num else "No")

main()
