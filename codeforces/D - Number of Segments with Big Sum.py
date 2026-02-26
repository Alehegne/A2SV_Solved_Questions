import sys
input = sys.stdin.readline

def solve():
    n,s = map(int,input().split())
    arr = list(map(int, input().split()))
    no=0
    curr=0
    left = 0
    for right,num in enumerate(arr):
        curr+=num
        no+=left
        while curr>=s:
            # print("fif:",num)
            no+=1
            curr-=arr[left]
            left+=1
    print(no)

solve()
