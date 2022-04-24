while True:
    N=list(map(int,input()))
    half=-1
    if N==[0]:
        break
    elif len(N)%2==0: ##짝수일경우
        half=int(len(N)/2)
        if N[:half]==N[:half-1:-1]:
            print("yes")
        else:
            print("no")
    else: ##홀수일경우
        half=int(len(N)/2)
        if N[:half]==N[:half:-1]:
            print("yes")
        else:
            print("no")
