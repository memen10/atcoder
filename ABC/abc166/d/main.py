import sys
input = lambda: sys.stdin.readline().strip()

def main():
    X = int(input())
    for diff in range(-200,200):
        for a in range(-200,200):
            b = a-diff
            if (a**5 - b**5) == X:
                break
        else:
            continue
        break
    print(a,b)

main()
