t=int(input())

for _ in range(t):

    n=int(input())

    piles=[]
    for _ in range(n):
        pile=list(map(int,input().split()))
        piles.append(pile)
    
    ops=0

    for i in range(len(piles)):

        if piles[i][0]>piles[i][2]:
            removedZeros=piles[i][0]-piles[i][2]
            ops+=removedZeros
            piles[i][0]-=removedZeros
        if piles[i][1]>piles[i][3]:
            removedOnes=piles[i][1]-piles[i][3]
            topZeros=piles[i][0]
            ops+=(removedOnes+topZeros)
    print(ops)

