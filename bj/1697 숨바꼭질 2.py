import sys
from collections import deque
N,K=map(int,sys.stdin.readline().split())

def bfs(start):
    queue=deque()
    l=[]
    queue.append([start])
    l.append(start)
    temp=[]
    cnt=0
    while queue:
        a=queue.popleft()
        cnt += 1

        for i in a:
            if i-1==K or i+1==K or i*2==K:
                print("유레카",i,l)
                return cnt
            if (i-1 not in  l) and i<K :
                temp.append(i-1)
                l.append(i-1)
            if (i+1 not in  l) and i<K:
                temp.append(i+1)
                l.append(i+1)
            if (i*2 not in  l) and i<K :
                temp.append(i*2)
                l.append(i*2)

        queue.append(temp)
        temp=[]



print(bfs(N))