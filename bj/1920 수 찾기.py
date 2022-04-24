import sys
N=int(sys.stdin.readline())
L=set(map(int,sys.stdin.readline().split()))
n=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
p=0
for i in l:
    if i in L:
        print(1)
    else:
        print(0)

# import sys
# L=[0 for i in range(4294967297)]
# N=int(sys.stdin.readline())
# c=list(map(int,sys.stdin.readline().split()))
# n=int(sys.stdin.readline())
# l=list(map(int,sys.stdin.readline().split()))
# for j in c:
#     L[j]=1
# for i in l:
#     if L[i]==1:
#         print(1)
#     else:
#         print(0)
