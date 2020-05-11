import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().strip()

def main():
    X = int(input())
    num_500 = int(X/500)
    num_5 = int((X%500)/5)
    print(int(num_500*1000 + num_5*5))

main()
