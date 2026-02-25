import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = arr[0:2]
    i = 2
    while i < len(arr):
        two = arr[i-2]
        one = arr[i-1]
        if one > two and arr[i] < one:
            ans.append(arr[i])
        elif one < two and arr[i] > one:
            ans.append(arr[i])
        else:
            ans.pop()
            ans.append(arr[i])
        i += 1
    print(len(ans))
    print(*ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
