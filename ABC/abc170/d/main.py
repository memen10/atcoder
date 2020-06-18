import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    N = I()
    A = numpy.array(sorted(LI()))

    b = A*numpy.invert(numpy.eye(N,dtype=bool)) # 対角要素を0にする
    b = b[b!=0].reshape(-1,N) # 対角要素削除
    print(b[:,0])
    print(numpy.mod(A[0],b[:,0]))
    print(numpy.mod(A,b))
    print(numpy.count_nonzero(numpy.mod(A,b),axis=0))
    print(N-numpy.any(numpy.mod(A,b)==0,axis=0).sum()) # N- 他要素で割り切れるAiの数

    # print(numpy.apply_along_axis(numpy.mod,0,A))

main()

