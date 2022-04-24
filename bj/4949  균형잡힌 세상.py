p=['(',')','[',']']
while True:
    b = []
    b_ = []
    b=input()
    if b==".":
        break

    for i in b:
        if i=="(" or i=="[":
            b_.append(i)
        elif i==")":
            if len(b_)!=0 and b_[-1]=="(":
                b_.pop()
            else:
                b_.append(i)
                break
        elif i=="]":
            if len(b_) != 0 and b_[-1] == "[":
                b_.pop()
            else:
                b_.append(i)
                break
    if len(b_)==0:
        print("yes")
    else:
        print("no")