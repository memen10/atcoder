import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def move_elem(A):
    A_part = A[:5]
    A_cnt = collections.Counter(A)
    A_most = A_cnt.most_common()[::-1]
    rm_list = []
    print(A_part)
    for a in A_most:
        if a in A_part:
            cnt = A_part.count(a)
            for _ in range(cnt):
                rm_list.append(a)
                if len(rm_list)==3:
                    break
    for e in rm_list:
        A_part.remove(e)
    return A_part+A[5::]

def main():
    N = I()
    A = LI()
    A_cnt = collections.Counter(A)
    A_most = A_cnt.most_common()
    print(A)
    print(move_elem(A))

main()

