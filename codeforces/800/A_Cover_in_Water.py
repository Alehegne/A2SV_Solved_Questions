

t=int(input())
for _ in range(t):

    n=int(input())
    cells = input()
    # print(cells)
    # count=0
    # if cells[0]==".":
    #     cells[0]="#"
    #     count+=1
    # for i in range(1,len(cells)):

    #     if cells[i-1]=="." and cells[i]==".":
    #         count+=1
    #         cells[i]="#"
    # print(count)
    if "..." in cells:
        print(2)
    else:
        print(cells.count("."))