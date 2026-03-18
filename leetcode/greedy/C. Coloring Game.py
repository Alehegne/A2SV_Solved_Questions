# def no_ways(n,a):
#     a.sort(reverse = True)
#     max_ = a[0]
#     ans = 0
#     for i in range(n-2):
#         curr_max = a[i]
#         ptr = i + 2
#         for j in range(i+1,n):
#             if curr_max >= a[j] * 2:
#                 break
#             #expand pointer
#             while ptr < n-1 and a[i] + a[j] + a[ptr] > max_ and a[j] + a[ptr] > curr_max:
#                 ptr += 1
#             #shrink
#             while ptr > j and a[i] + a[j] + a[ptr] <= max_ or a[j] + a[ptr] <= curr_max:
#                 ptr -= 1
#             if ptr > j:
#                ans += ptr - j
            
#     return ans
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int,input().split()))
#     ways = no_ways(n,a)
#     print(ways)
# refactored
def no_ways(n, arr):
    arr.sort(reverse=True)
    ans = 0
    max_ = arr[0]
    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:

            # check both conditions
            if (arr[left] + arr[right] > arr[i] and
                arr[i] + arr[left] + arr[right] > max_):

                # all elements between left+1 ... right also work
                ans += (right - left)
                left += 1
            else:
                right -= 1

    return ans
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    ways = no_ways(n,a)
    print(ways)
