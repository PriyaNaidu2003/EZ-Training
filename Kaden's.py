d=list(map(int,input().split()))
curr_sum=0
c_sum=0
m_sum=0
for i in range(len(d)):
    curr_sum=curr_sum+d[i]
    if curr_sum<0:
        curr_sum=0
    if curr_sum>c_sum:
        c_sum=curr_sum
    if curr_sum>m_sum:
        m_sum=curr_sum
print(m_sum)
