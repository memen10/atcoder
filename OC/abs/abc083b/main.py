import sys
input = lambda: sys.stdin.readline().strip()

def main():
    N, A, B = map(int, input().split())

    all_sum = 0
    for i in range(1,N+1):
        keta_sum = sum(list(map(int, str(i))))
        if keta_sum >= A and keta_sum <= B:
            all_sum += i
    print(all_sum)

main()
