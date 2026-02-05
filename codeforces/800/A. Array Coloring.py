
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    for i in range(n):
        if s[i] == ')' and i < n - 1:
            res = 2 + 2*i
            print(res if res < n else -1)
            break
    else:
        print(-1)
