
t=int(input())

for _ in range(t):
    n,x=map(int,input().split())
    ints=list(map(int,input().split()))
    # min_=float('-inf')

    # for i in range(len(ints)+1):
    #     if i==len(ints):
    #         min_=max(min_,2*(x-ints[i-1]))
    #     elif i==0:
    #         min_=max(min_,ints[i])
    #     else:
    #         min_=max(min_,ints[i]-ints[i-1])
    # print(min_)
    #cleaner
    max_gap=ints[0]
    for i in range(1,len(ints)):
        max_gap=max(max_gap,ints[i]-ints[i-1])
    max_gap=max(max_gap,2*(x-ints[-1]))
    print(max_gap)