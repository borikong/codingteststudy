import sys,heapq
N=int(sys.stdin.readline())
heap=[]
for i in range(N):
    c=int(sys.stdin.readline())
    if c!=0:
        heapq.heappush(heap,[abs(c),c])
        # print(heap)
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
