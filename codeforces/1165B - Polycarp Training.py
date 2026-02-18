import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    # problem = 1
    # count = 0
    # i = 0
    # while i < len(arr):
    #     while i<len(arr)-1 and problem > arr[i]:
    #         i += 1
    #     if problem <= arr[i]:
    #         count += 1
    #     problem += 1
    #     i += 1
    # print(count)
    day = 1
    for problem in arr:
        if problem >= day:
            day += 1
    print(day - 1)
def main():
    solve()

if __name__ == "__main__":
    main()
