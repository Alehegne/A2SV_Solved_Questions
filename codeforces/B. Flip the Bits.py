
def solve():
    n = int(input())
    a = input()
    b = input()

    c_0 = a.count("0")
    c_1 = a.count("1")

    flip = False
    for i in range(n-1,-1,-1):
        if (flip and a[i]==b[i]) or (not flip and a[i] != b[i]):
            if c_0 != c_1:
                print("NO")
                return
            else:
                flip = not flip
        if a[i] == "0":
            if flip:  c_1 -= 1
            else:  c_0 -= 1
        else:
            if flip:  c_0 -= 1
            else:  c_1 -= 1
        # print(c_0,c_1)
    print("YES")

t = int(input())
for _ in range(t):
    solve()


