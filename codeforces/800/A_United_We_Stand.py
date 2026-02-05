from collections import Counter

def solve():

    n = int(input())
    a = list(map(int,input().split()))

    freq = Counter(a)
    if len(freq)==1:
        print(-1)
        return
    b = []
    c = []
    max_=max(a)
    for i in range(len(a)):
        if a[i]!=max_:
            b.append(a[i])
        else:
            c.append(a[i])
    if len(b)==0:
        print(-1)
    else:
        print(len(b)," ",len(c))
        print(*b)
        print(*c)








t=int(input())
for _ in range(t):
    solve()
