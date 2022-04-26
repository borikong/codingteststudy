import sys
N,r,c=map(int,sys.stdin.readline().split())

def divide(x,y,size,number):
    if size>2:
        if x<size/2 and y<size/2:
            number=divide(x,y,size/2,number+0)
        elif x>=size/2 and y<size/2:
            number=divide(x-size/2,y,size/2,number+size/2*size/2)
        elif x<size/2 and y>=size/2:
            number=divide(x,y-size/2,size/2,number+size*size/2)
        elif x>=size/2 and y>=size/2:
            number=divide(x-size/2,y-size/2,size/2,number+size*size-(size/2)*(size/2))
        return number
    else:
        for i in range(2):
            for j in range(2):
                if i==y and j==x:
                    return number
                else:
                    number+=1

ans=divide(c,r,2**N,0)
print(int(ans))
