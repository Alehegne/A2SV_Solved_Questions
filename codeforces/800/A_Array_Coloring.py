t=int(input())

for _ in range(t):
    n=int(input())

    nums=list(map(int,input().split(" ")))

    sum_=sum(nums)

    if sum_%2==0:
        print("YES")
    else:
        print("NO")