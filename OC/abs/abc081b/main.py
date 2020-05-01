import numpy as np

def main():
    N = int(input())
    lst = np.array(list(map(int, input().split())))
    cnt = 0
    while (lst%2==0).all():
        cnt += 1
        lst = lst/2
    print(cnt)

main()
