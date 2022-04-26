import sys
import heapq
N=int(sys.stdin.readline())
heap=[]
for i in range(N):
    num=int(sys.stdin.readline())
    if num==0:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap,num)