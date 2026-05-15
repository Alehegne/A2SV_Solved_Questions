import sys
import math
import bisect
from heapq import heappush,heappop,heappushpop,heapreplace,heapify
from collections import defaultdict, deque, Counter

sys.setrecursionlimit(10**7)

def debug(*args):
    print("DEBUG:", *args)

input = lambda: sys.stdin.readline().rstrip()
rint = lambda: int(input())
rints = lambda: list(map(int, input().split()))
rstr = lambda: input()
rstrs = lambda: input().split()

def r_arrs():
    n = rint()
    arr = rints()
    return arr, n

freq = lambda arr: Counter(arr)
YES = lambda: print("YES")
NO = lambda: print("NO")

def p_arr(arr):
    print(*arr)

INF = float('inf')
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            if self.size[rootA] < self.size[rootB]:
                self.parent[rootA] = rootB
                self.size[rootB] += self.size[rootA]
            else:
                self.parent[rootB] = rootA
                self.size[rootA] += self.size[rootB]
# main solve
def solve():
    n,m = rints()
    edges = []
    for _ in range(m):
        b,e,w = rints()
        edges.append((w,b,e))
    edges.sort()
    uf = UnionFind(n+1)
    ans = 0
    for w,b,e in edges:
        if uf.find(b) == uf.find(e):
            continue
        uf.union(b,e)
        ans += w
    print(ans)

solve()
