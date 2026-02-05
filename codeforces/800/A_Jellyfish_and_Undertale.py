

def solve():

    max_, initial, tool_total = list(map(int,input().split()))
    tools = list(map(int,input().split()))
    total_sec = initial
    for i in range(len(tools)):
        total_sec += max_- 1 if tools[i]>=max_ else tools[i]
    print(total_sec)

t = int(input())
for _ in range(t):
    solve()