import sys
import numpy as np
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().strip()

def main():
    K = int(input())
    num_list = np.array([i for i in range(1,K+1)])
    print(np.sum(np.gcd.outer(np.gcd.outer(num_list,num_list),num_list)))

main()
