t=int(input())

for _ in range(t):

    n=int(input())
    names=input().split()
    s=names[0]
    for i in range(1,len(names)):

        s=(s+names[i]) if (s+names[i])<(names[i]+s) else (names[i]+s)
    print(s)


