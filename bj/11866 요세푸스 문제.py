import sys,math
N,K=map(int,sys.stdin.readline().split())

queue=[i for i in range(1,N+1)]
q=[]
n=0
while len(q)<N:
    n=(n+K-1)%len(queue)
    q.append(str(queue.pop(n)))

print("<"+", ".join(q)+">")
