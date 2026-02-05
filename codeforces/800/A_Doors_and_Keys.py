def solve():
    dor_key = input()
    keys = set(['r','b','g'])
    doors = set(["R","B","G"])
    vis_key = set()
    for ch in dor_key:
        if ch in keys:
            vis_key.add(ch)
        if ch  in doors:
            if ch.lower() not in vis_key:
                print("NO")
                return
    print("YES")

t=int(input())
for _ in range(t):
    solve()