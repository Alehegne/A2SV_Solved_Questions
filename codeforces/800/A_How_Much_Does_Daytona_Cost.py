
t = int(input())

for _ in range(t):
    n,k=list(map(int,input().split()))
    nums=list(map(int,input().split()))

    if k in nums:
        print("YES")
    else:
        print("NO")