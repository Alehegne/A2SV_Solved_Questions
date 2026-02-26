# refactor this code later, its highly bloated

import sys
input = sys.stdin.readline
from collections import Counter
def solve():
    n,l,ri = map(int,input().split())
    arr = list(map(int, input().split()))
    left = Counter(arr[:l])
    right = Counter(arr[l:])
    cost = 0
    #no cost for similiar pair
    for l in left:
        if l in right:
            min_ = min(left[l],right[l])
            left[l] -= min_
            right[l] -= min_
    left_sum = sum(left.values())
    right_sum = sum(right.values())
    if left_sum == right_sum:
        cost += left_sum
        print(cost)
        return
    if right_sum > left_sum:
        decrement = right_sum - left_sum#from right, decrement till decrement==0
        for r in right.most_common():
            if r[1] > decrement:
                right[r[0]] -= decrement
                cost += decrement//2 + decrement % 2
                right_sum-=decrement
                break
            else:
                cost += r[1]//2
                if not r[1] % 2:
                    decrement -= r[1]
                    right_sum -= r[1]
                else:
                    decrement -= (r[1] - 1)
                    right_sum -= (r[1] - 1)
                if decrement <= 0:
                    break
    else:
        # for l in left:
        decrement = left_sum - right_sum#from right, decrement till decrement==0
        for r in left.most_common():
            if r[1] > decrement:
                left[r[0]] -= decrement
                cost += decrement//2 + decrement % 2
                left_sum -= decrement
                break
            else:
                cost += r[1]//2
                if not r[1] % 2:
                    decrement -= r[1]
                    left_sum -= r[1]
                else:
                    decrement -= (r[1] - 1)
                    left_sum -= (r[1] - 1)
                if decrement <= 0:
                    break
    cost += max(right_sum,left_sum)
    print(cost)
t = int(input())
for _ in range(t):
    solve()
