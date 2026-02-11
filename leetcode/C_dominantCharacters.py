def solve():
    n = int(input())
    s = input().strip()
    
    ans = float('inf')
    
    for i in range(n):
        a = b = c = 0
        
        # only check next 7 characters
        for j in range(i, min(n, i + 7)):
            if s[j] == 'a':
                a += 1
            elif s[j] == 'b':
                b += 1
            else:
                c += 1
            
            length = j - i + 1
            
            if length >= 2 and a > b and a > c:
                ans = min(ans, length)
    
    print(ans if ans != float('inf') else -1)

t = int(input())
for _ in range(t):
    solve()
