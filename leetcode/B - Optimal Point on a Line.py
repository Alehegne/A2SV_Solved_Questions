
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    #find median
    index = (n)//2
    if not n %2:
        print(arr[index-1])
        return
    print(arr[index])

def main():

    solve()

if __name__ == "__main__":
    main()
