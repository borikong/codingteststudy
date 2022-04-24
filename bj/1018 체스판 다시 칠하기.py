N,M=map(int,input().split())
chess=[]
miss=0
miss_list=[]
for i in range(N):
    chess.append(list(input()))

def make_chess(chess,color):
    miss=0
    # 첫번째 줄이 color로 시작
    if chess[0][0] != color:
        chess[0][0] = color
        miss+=1

    for i in range(8):
        if i != 0:
            if chess[i][0] == chess[i - 1][0]:
                if chess[i][0] == 'W':
                    chess[i][0] = 'B'
                    miss += 1
                else:
                    chess[i][0] = "W"
                    miss += 1
        for j in range(7):
            if chess[i][j] == chess[i][j + 1]:
                if chess[i][j] == 'W':
                    chess[i][j + 1] = 'B'
                    miss += 1
                else:
                    chess[i][j + 1] = 'W'
                    miss += 1
    return miss

miss=make_chess([row[:8] for row in chess[:8]] ,'W')

for i in range(N-8+1):
    for j in range(M-8+1):
        miss_list.append(make_chess([row[j:j+8] for row in chess[i:i+8]],'W'))
        miss_list.append(make_chess([row[j:j + 8] for row in chess[i:i + 8]], 'B'))

print(min(miss_list))


