inp=input()
msg="hello"
#ahhellllloou
#xqjqmenkodmlhzyzmmvofdngktygbbxbzpluzcohohmalkoeuwfikblltaaigv
idx=0

for i,c in enumerate(inp):
    if idx==4 and inp[i]=='o':
        print("YES")
        break
    if inp[i]==msg[idx]:
        idx+=1

else:
    print("NO")

