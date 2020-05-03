import math
import sys
input = lambda: sys.stdin.readline().strip()

def main():
    X = int(input())
    n = 100
    for i in range(1,4000):
        n = int(n*1.01)
        if n>=X:
            break
    print(i)

main()
