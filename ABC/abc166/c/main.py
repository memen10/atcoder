import collections
import sys
input = lambda: sys.stdin.readline().strip()

def main():
    N,M = map(int,input().split())
    H_list = list(map(int,input().split()))
    ab_list = [map(int,input().split()) for _ in range(M)]

    ab_dict = dict()
    for a,b in ab_list:
        minab = min(a,b)
        maxab = max(a,b)
        if str(minab) not in ab_dict.keys():
            ab_dict.update({minab:[maxab]})
        else:
            ab_dict[str(minab)] += maxab
        if str(maxab) not in ab_dict.keys():
            ab_dict.update({maxab:[minab]})
        else:
            ab_dict[str(maxab)] += minab

    c = collections.Counter(H_list)

    print(H_list)
    print(ab_dict)
    ans = 0
    for k in ab_dict.keys():
        if k > min(ab_dict.get(k)):
            ans += c[k]
        else:
            ans += c[k]

    print(ans)

main()
