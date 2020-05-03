import sys
input = lambda: sys.stdin.readline().strip()

def main():
    X = int(input())

    for a in range(-120,120):
        if (a**5 - (a-1)*5) == X:
            print(X)
            break
    print(a,(a-1))

# def factorization(n):
#     arr = []
#     temp = n
#     for i in range(2, int(-(-n**0.5//1))+1):
#         if temp%i==0:
#             cnt=0
#             while temp%i==0:
#                 cnt+=1
#                 temp //= i
#             # arr.append([i, cnt])
#             arr.append(i**cnt)
#
#     if temp!=1:
#         # arr.append([temp, 1])
#         arr.append(temp)
#
#     if arr==[]:
#         # arr.append([n, 1])
#         arr.append(n)
#     return arr
#
# def main():
#     N = int(input())
#     n_fac = factorization(N)
#     mi = min(n_fac)
#     ma = max(n_fac)
#     # print(n_fac)
#     # print(mi)
#     y = -5
#     x = None
#     while True:
#         if mi**4 -3*mi**3*y + 10*mi**2*y**2 + 2*mi*y**3 + 5*y**4 == ma:
#             x = y + mi
#             break
#         else:
#             y += 1
#     print(x,y)
main()
