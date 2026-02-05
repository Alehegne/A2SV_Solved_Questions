
t=int(input())

for _ in range(t):

    n=int(input())
    a=list(map(int,input().split()))
    ops=0
    isValid=True
    print(a)
    for i in range(1,len(a)):
        if a[i]==1:
            isValid=False
            break
        if not isValid:
            break
        #look back
        idx=i-1
        while True:
            if a[idx]<a[idx+1]:
                break
            # print(a[idx],":",a[idx+1])
            while a[idx]>=a[idx+1]:
                a[idx]=a[idx]//2
                ops+=1
            if a[idx]==1 and idx!=0:
                isValid=False
                break
            if idx>0:
                prev=idx-1
                if a[prev]<a[idx]:
                    break
                idx=idx-1
    print(a)
    if isValid:
        print(ops)
    else:
        print(-1)

        