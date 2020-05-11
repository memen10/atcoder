import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().strip()

def main():
    K,N = map(int,input().split())
    A_list = list(map(int,input().split()))
    dist_list = []
    A_list.append(K)
    for i in range(1,len(A_list)):
        dist_list.append(A_list[i]-A_list[i-1])
    d_sorted = sorted(dist_list)
    print(int(sum(d_sorted[0:N-1])))

main()
