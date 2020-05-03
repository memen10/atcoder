# k=int(input());
# a,b=map(int,input().split())
# is_ok = False
# for i in range(1,int(b/k)+1):
#     if a<=i*k<=b:is_ok=True
#     else: pass
# print("OK" if is_ok==True else "NG")
# ----------------------------------------
#k=int(input());a,b=map(int,input().split());print("ONKG"[int(b/k)*k<a::2])
k,a,b=map(int,open(0).read().split());print("ONKG"[b<b%k+a::2])

