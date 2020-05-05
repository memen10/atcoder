import sys
input = lambda: sys.stdin.readline().strip()

def main():
    N = int(input())
    a_lst = map(int, input().split())

    a_lst = sorted(a_lst)
    alice_score = 0
    bob_score = 0
    for _ in range(0,N,2):
        alice_score += a_lst.pop() if a_lst else 0
        bob_score += a_lst.pop() if a_lst else 0
    print(alice_score - bob_score)

main()
