import collections
import sys
input = lambda: sys.stdin.readline().strip()

def main():
    N,M = map(int,input().split())
    H_list = list(map(int,input().split()))
    ab_list = [list(map(int,input().split())) for _ in range(M)]

    ab_dict = {i: [] for i in range(N)}
    for a,b in ab_list:
        a,b = a-1,b-1
        ab_dict[a].append(b)
        ab_dict[b].append(a)

    ans = 0
    for k,v_list in ab_dict.items():
        for v in v_list:
            if H_list[v] >= H_list[k]:
                break
        else:ans += 1
    print(ans)

main()
