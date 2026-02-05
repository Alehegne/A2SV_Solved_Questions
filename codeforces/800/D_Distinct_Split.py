from collections import Counter
def solve():
    max_=float('-inf')
    n=int(input())
    words=input()
    left=set()
    right=Counter(words)
    # right=set(words)
    for i in range(len(words)):
        left.add(words[i])
        right[words[i]]-=1
        if right[words[i]]==0:
            del right[words[i]]
        max_=max(len(left)+len(right),max_)
    print(max_)
t=int(input())
for _ in range(t):
    solve()