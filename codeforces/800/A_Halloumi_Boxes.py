t = int(input())
n,s=map(int,input().split(" "))
for _ in range(n):
    nums=list(map(int,input().split(" ")))
    seg=[nums[0]]

    for i,num in enumerate(1,nums):
        if s>len(seg) and nums[i]<nums[i-1]:
            #add to segment
        else:
            #sort all segs
            





