
n=int(input())
nums=list(map(int,input().split()))
min_=min(nums,key=lambda num:abs(num))
print(abs(min_))