import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def get_p_list(nowh,noww,range):
    p_list = []
    for h in range(nowh-range,nowh+range):
        for w in range(noww-range,noww+range):
            if h>=0 and w>=0:
                p_list.append((h,w))
    return p_list

def can_move(nowh,noww,S):



def main():
    H, W = LI()
    Ch,Cw = LI()
    Dh,Dw = LI()
    S = [LS() for _ in range(H)]
    # print(Ch,Cw)
    # print(get_p_list(Ch,Cw,2))





main()

