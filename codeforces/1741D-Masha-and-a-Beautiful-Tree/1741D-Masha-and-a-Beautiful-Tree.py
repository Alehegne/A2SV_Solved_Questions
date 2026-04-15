import sys
import math
import bisect
from collections import defaultdict, deque, Counter

sys.setrecursionlimit(10**7)

def debug(*args):
    print("DEBUG:", *args)

input = lambda: sys.stdin.readline().rstrip()
rint = lambda: int(input())
rints = lambda: list(map(int, input().split()))
rstr = lambda: input()
rstrs = lambda: input().split()

def r_arrs():
    n = rint()
    arr = rints()
    return arr, n

freq = lambda arr: Counter(arr)
YES = lambda: print("YES")
NO = lambda: print("NO")

def pa(arr):
    print(*arr)

INF = float('inf')

# main solve
def solve():
    m = rint()
    p = rints()

    ops = 0
    pos = True
    def merge(left,right):
        nonlocal ops
        nonlocal pos
        #check non-overlapping
        if left[-1] <= right[0]:
            return left + right
        elif right[-1] <= left[0] and pos:
            ops += 1
            return right + left
        pos = False
        return left + right  
    def merge_s(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr)//2
        left = merge_s(arr[:mid])
        right = merge_s(arr[mid:])
        return merge(left,right)
    merge_s(p)
    if pos:
        print(ops)
    else:
        print(-1)
t = rint()
for _ in range(t):
    solve()