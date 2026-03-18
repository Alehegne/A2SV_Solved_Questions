def no_ways(n,a):
    a.sort(reverse = True)
    max_ = a[0]
    ans = 0
    for i in range(n-2):
        curr_max = a[i]
        ptr = i + 2
        for j in range(i+1,n):
            if curr_max >= a[j] * 2:
                break
            #expand pointer
            while ptr < n-1 and a[i] + a[j] + a[ptr] > max_ and a[j] + a[ptr] > curr_max:
                ptr += 1
            #shrink
            while ptr > j and a[i] + a[j] + a[ptr] <= max_ or a[j] + a[ptr] <= curr_max:
                ptr -= 1
            if ptr > j:
               ans += ptr - j
            
    return ans
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    ways = no_ways(n,a)
    print(ways)
