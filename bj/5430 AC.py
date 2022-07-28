#R 뒤집기, D 버리기
#R 배열의 수의 순서를 뒤집는 함수, D는 첫번쨰 수를 버리는 함수
#빈 배열에 D 사용시 에러
import sys
from collections import deque

T=int(sys.stdin.readline())

for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    li = sys.stdin.readline().strip()
    if n > 0:
        li = deque(map(int, li[1:-1].split(",")))
    else:
        li = deque()

    error=False
    flag=-1 #-1이면 왼쪽에서 pop 1이면 오른쪽에서 pop
    cnt=0 #reverse 횟수 세는 변수

    for command in p:
        if command=="R":
            ## 시간복잡도 O(N)
            ##li.reverse()
            cnt=cnt+1
            flag*=-1

        elif command=="D":
            if len(li)!=0:
                if flag==-1:
                    li.popleft()
                else:
                    li.pop()
            else:
                error=True
                break


    if error:
        print("error")
    else:
        l=len(li)
        if l==0:
            print("[]")
        elif l==1:
            print("[",*li,"]",sep="")
        else:
            if cnt%2==0: ##R을 2로 나눈 나머지가 0이라면 원래대로
                print("[",end="")
                for i in range(len(li)-1):
                    print(li[i],",",sep="",end="")
                print(li[-1],"]",sep="")
            else:
                print("[", end="")
                for i in range(len(li)-1,0,-1):
                    print(li[i], ",", sep="", end="")
                print(li[0], "]", sep="")
