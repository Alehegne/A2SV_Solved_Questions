
def solve():
    s = input()
    w = set()
    i = 0
    n = len(s)
    while i < len(s):
        if i+1 < n and s[i+1] == s[i]:
            i += 1
        else:
            w.add(s[i])
        i += 1
    print("".join(sorted(w)))
t = int(input())
for _ in range(t):
    solve()
