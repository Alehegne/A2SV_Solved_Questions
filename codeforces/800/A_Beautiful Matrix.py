


matrix = [list(map(int,input().split())) for _ in range(5)]
pos = ()
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            pos = (i,j)
# print(i,j)
print(abs(2-pos[0])+abs(2-pos[1]))
