import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().strip()

def main():
    N = int(input())
    S_list = [input() for _ in range(N)]
    print(len(list(set(S_list))))

main()
