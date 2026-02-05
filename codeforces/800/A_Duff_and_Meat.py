


n=int(input())
m_ps=[]
for _ in range(n):
    m_p=list(map(int,input().split()))
    m_ps.append(m_p)
min_ex=m_ps[0][0]*m_ps[0][1]
cheap=0

for i in range(1,n):
    if m_ps[i][1]>m_ps[cheap][1]:
        min_ex+=m_ps[i][0]*m_ps[cheap][1]
    else:
        min_ex+=m_ps[i][0]*m_ps[i][1]
        cheap=i
print(min_ex)


    