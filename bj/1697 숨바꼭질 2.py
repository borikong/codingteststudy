import sys
from collections import deque
N,K=map(int,sys.stdin.readline().split())

def bfs(start):
    queue=deque()
    queue.append(start)
    temp[start]=0

    while queue:
        a=queue.popleft()
        for i in [a-1,a+1,a*2]:
            if -1<i<100001:
                if temp[i]==0 and i!=start:
                    temp[i]=temp[a]+1
                    queue.append(i)
                if i==K:
                    return temp[K]



temp=[0 for i in range(100002)]
print(bfs(N))