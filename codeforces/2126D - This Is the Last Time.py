import sys
input = sys.stdin.readline

def solve():
    n,k = map(int,input().split())
    casinos = list(list(map(int,input().split())) for _ in range(n))
    casinos.sort(key=lambda x:(x[0],x[1]))
    for casino in casinos:
        if k < casino[0]:
            print(k)
            return
        if casino[0] <= k <= casino[1]:
            k = max(k,casino[2])
    print(k)


def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
