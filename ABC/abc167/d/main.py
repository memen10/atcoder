import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().strip()

def main():
    N,K = map(int,input().split())
    A_list = list(map(int,input().split()))
    A_narabikae_list = [1]
    A_kako = [1]
    idx = 1-1
    for ai in A_list:
        A_narabikae_list.append(A_list[idx])
        if A_list[idx] in A_kako:
            rep_start = A_narabikae_list.index(A_list[idx])
            A_kako = A_kako[rep_start::]
            rep_end = rep_start + len(A_kako) -1
            break
        A_kako.append(A_list[idx])
        idx = A_list[idx]-1
    A_kako_idx = (K-rep_start)%(rep_end-rep_start+1)
    print(A_kako[A_kako_idx])

main()
