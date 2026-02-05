

def solve():

    n,k=list(map(int,input().split()))
    if k==0:
        print(*[i for i in range(1,n+1)])
        return
    if n==2 and k==1:
        print(-1)
        return
    if k>=n/2:
        print(-1)
        return
    peaks = []
    for i in range(n,n-k,-1):
        peaks.append(i)
    # print("peaks:",peaks)
    ans=[]
    num=1
    for i in range(1,n+1):
        if i%2==0 and len(peaks)>0:
            ans.append(peaks.pop())
        else:
            ans.append(num)
            num+=1
    print(*ans)


t=int(input())
for _ in range(t):

    solve()