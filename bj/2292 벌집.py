N=int(input())

if N==1:
    print(1)
else:
    num=(3+(9-4*3*(1-N))**(1/2))/6
    if num%1!=0:
        print(int(num)+1)
    else:
        print(int(num))
