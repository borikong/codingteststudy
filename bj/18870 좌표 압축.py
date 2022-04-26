import sys
N=int(sys.stdin.readline())
num=list(map(int,sys.stdin.readline().strip().split()))
ss=list(set(num))
ss.sort()
dic={ss[i]:i for i in range(len(ss))}

for i in num:
    print(dic[i],end=" ")
