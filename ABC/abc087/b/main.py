
import sys
input = lambda: sys.stdin.readline().strip()

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())
    # A, B, C, X = map(int,open(0))

    cnt = 0
    for i_a in range(min(int(X/500),A)+1):
        X_a = X-500*i_a
        for i_b in range(min(int(X_a/100),B)+1):
            X_b = X_a - 100*i_b
            for i_c in range(min(int(X_b/50),C)+1):
                X_c = X_b - 50*i_c
                if X_c==0:
                    cnt += 1
    print(cnt)

main()
