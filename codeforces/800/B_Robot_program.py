import math
def solve():
    n,x,k = map(int,input().split())
    com = input()
    i = 0

    #first zero
    while i < len(com) and x!=0:
        if com[i] == "L":
            x -= 1
        elif com[i] == "R":
            x += 1
        i += 1
    #check a one-time command termination
    if i == len(com) and x != 0:
        print(0)
        return
    #find the next zero, when it starts from x = 0
    #if we get another pos in command for zero, that runs foreever
    #as long as it has time
    #in the above we have +1 zero turn
    j = 0
    #first zero
    while j < len(com):
        if com[j] == "L":
            x -= 1
        elif com[j] == "R":
            x += 1
        j += 1
        if x == 0:
            break
    #command finishes with out iterative
    if j == len(com) and x != 0:
        print(1)#only the first
        return
    total = (k - i)//j + 1
    print(total)
    


def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
