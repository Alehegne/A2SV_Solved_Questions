
t=int(input())

for _ in range(t):

    n=int(input())
    goals=list(map(int,input().split()))

    sum_=sum(goals)

    print(-sum_)