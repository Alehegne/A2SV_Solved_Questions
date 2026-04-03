# re-usable python template for Codeforces
import sys
import math
import bisect
from collections import defaultdict, deque, Counter
sys.setrecursionlimit(10**7)
#debugging
def debug(*args):
    print("DEBUG:", *args)

# fast input
input = lambda: sys.stdin.readline().rstrip()
rint = lambda: int(input())
rints = lambda: list(map(int, input().split()))
rstr = lambda: input()
rstrs = lambda: input().split()

def r_arrs():
    n = rint()
    arr = rints()
    return arr, n

# binary search
def b_search(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

# lower / upper bound
def l_bound(arr, x):
    return bisect.bisect_left(arr, x)

def u_bound(arr, x):
    return bisect.bisect_right(arr, x)

# check function (for binary search problems)
def check(mid):
    # implement the check logic here for binary search
    return True

# frequency
freq = lambda arr: Counter(arr)

# output helpers
YES = lambda: print("YES")
NO = lambda: print("NO")

def p_arr(arr):
    print(*arr)

# directions
DIR4 = [(0,1),(0,-1),(1,0),(-1,0)]
DIR8 = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

# prefix sum
def prefix_sum(arr):
    pre = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        pre[i+1] = pre[i] + arr[i]
    return pre

# constants
INF = float('inf')
MOD = 10**9 + 7


# main solve
def solve():
    n,m = rints()
    a = rints()
    b = rints()
    #sort b
    b.sort()

    #minimize the first element
    a[0] = min(a[0], b[0] - a[0])


    for i in range(1,n):
        best = float('inf')

        if a[i] >= a[i-1]:
            best = min(best, a[i])

        sm = a[i] + a[i-1]
        #find a value in b that is >= sm
        idx = l_bound(b, sm)
        if idx < m:
            best = min(best, b[idx] - a[i])
        if best == float('inf'):
            NO()
            return
        a[i] = best
    YES()
    

        




# multi-testcase
def main():
    t = rint()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()