T=int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    floor=N%H if N%H!=0 else H
    room=(N//H)+1 if N%H!=0 else N//H
    print(floor*100+room)
