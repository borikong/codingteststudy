import sys
N=int(sys.stdin.readline())
graph=[[] for _ in range(N)]
for i in range(N):
    a=str(sys.stdin.readline().strip())
    for j in a:
        graph[i].append(int(j))

li=[]
def divide(x,y,size):
    start=graph[y][x]
    if size==1:
        li.append(start)
        return 2
    for i in range(y,y+size):
        for j in range(x,x+size):
            if graph[i][j]!=start:
                li.append("(")
                half=int(size/2)
                divide(x,y,half)
                divide(x+half,y,half)
                divide(x,y+half,half)
                divide(x+half,y+half,half)
                li.append(")")
                return
    li.append(start)
    return size

divide(0,0,N)
print(*li,sep="")
