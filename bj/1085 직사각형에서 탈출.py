x,y,w,h=map(int,input().split())
d=[h-y,x,y,w-x]
print(min(d))