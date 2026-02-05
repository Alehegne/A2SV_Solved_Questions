n,m=map(int,input().split())


if m%n!=0:
    print(-1)
else:
    res=m/n
    move=0

    while res>1 and res%3==0:
        move+=1
        res=res/3
    while res>1 and res%2==0:
        move+=1
        res=res/2
    if res==1:
        print(move)

    else:
        print(-1)

    
