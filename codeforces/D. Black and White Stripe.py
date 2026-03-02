def solve():

    n,k = map(int,input().split())
    st = input().strip()

    bc = 0
    wc = 0

    min_ = 10**18
    left = 0

    for r,color in enumerate(st):
        if color == "W":
            wc += 1
        size = r - left + 1
        if size == k:
            min_ = min(min_,wc)
            if st[left] == "W":
                wc -= 1
            left += 1
    print(min_)
        
t = int(input())
for _ in range(t):
    solve()
