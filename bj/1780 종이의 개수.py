import sys
L=int(sys.stdin.readline())
paper=[list(map(int,sys.stdin.readline().split())) for i in range(L)]
num=[0,0,0]##-1,0,1
def divide(x,y,size):
    start=paper[y][x]
    for i in range(y,y+size):
        for j in range(x,x+size):
            if paper[i][j]!=start:
                divide(x, y, size // 3)
                divide(x, y + size // 3 * 1, size // 3)
                divide(x, y + size // 3 * 2, size // 3)

                divide(x + size // 3 * 1, y, size // 3)
                divide(x + size // 3 * 1, y + size // 3 * 1, size // 3)
                divide(x + size // 3 * 1, y + size // 3 * 2, size // 3)

                divide(x + size // 3 * 2, y, size // 3)
                divide(x + size // 3 * 2, y + size // 3 * 1, size // 3)
                divide(x + size // 3 * 2, y + size // 3 * 2, size // 3)
                return

    num[start+1]+=1


divide(0,0,L)
print(*num,sep="\n")