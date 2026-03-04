def solve():
    n = int(input())
    aint = list(map(int,input().split()))
    m = int(input())
    mint = list(map(int,input().split()))

    ap = [0]*(n+1)
    for i in range(1,n+1):
        ap[i] += ap[i-1] + aint[i-1]
    max_ = max(ap)
    mp = [0] * (m+1)
    for i in range(1,m+1):
        mp[i] += mp[i-1] + mint[i-1]
    max_m = max(mp)
    print(max(0,max_+max_m))

    

    
t = int(input())
for _ in range(t):
    solve()
