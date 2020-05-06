import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().strip()

def main():
    N = int(input())
    A_list = list(input().split())
    buka_dict = {str(i+1): 0 for i in range(N)}
    for i in A_list:
        buka_dict[str(i)] += 1
    for i in buka_dict.values():
        print(i)


main()
