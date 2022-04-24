#divide and conquer
import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = []

def solution(x, y, N) :
  color = paper[x][y]
  for i in range(x, x+N) :
    for j in range(y, y+N) :
      if color != paper[i][j] : #각 작은 종이의 색이 시작 종이의 색과 다르면 쪼갬
        #divide
        solution(x, y, N//2) ##1사분면
        solution(x, y+N//2, N//2) ##2사분면
        solution(x+N//2, y, N//2) ##3사분면
        solution(x+N//2, y+N//2, N//2) ##4사분면
        return ##conquer
    #사각형 색이 모두 같으면 첫 번째 종이조각 색이 뭔지 구별해서 result에 추가
  if color == 0 :
    result.append(0)
  else :
    result.append(1)


solution(0,0,N) ##0,0 부터 시작
print(result.count(0))
print(result.count(1))