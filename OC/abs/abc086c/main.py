import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().strip()

def main():
    N = int(input())
    tx_list = [list(map(int,input().split())) for _ in range(N)]

    pre_ti, pre_x, pre_y = 0,0,0
    for tx in tx_list:
        ti,x,y = tx[0],tx[1],tx[2]
        tmp_ti,tmp_x,tmp_y = ti-pre_ti,x-pre_x,y-pre_y
        pre_ti,pre_x,pre_y = ti,x,y
        for i in range(tmp_ti+1):
            if ((tmp_ti-i)-i) == (abs(tmp_x)+abs(tmp_y)):
                break
        else:
            print("No")
            exit()
    print("Yes")

main()