# N=int(input())
# p=[]
# for i in range(N):
#     p.append(list(map(int,input().split())))
# p.sort()
# for i in range(N):
#     print(*p[i])
import sys
a = sys.stdin.readlines()[1:]
a.sort(key=lambda x:(int(x.split()[0]), int(x.split()[1])))
print(''.join(a))