def gate(lst):
    flag=False
    for i in range(len(lst)):
        ls=sum(lst[0:i])
        rs=sum(lst[i:])
        if ls==rs:
            flag=True
            eq_gate=i
            break
    if flag:
        return (eq_gate)
    else:
        if len(lst)%2==0:
            mid=len(lst)//2-1
        else:
            mid=len(lst)//2
        return (mid)
    
i_p=[
    [2,2,1,2,1],
    [4,2,3,1,2,1,2,3],
    [1,1,1,1,1],
    [3,0,3],
    [1,2,1,1,2,1],
    [1,1,1,2,1],
    [5,2,1,3,1,2,5]
    ]
result={}
for i in i_p:
    st="Checkpoint"+str(i_p.index(i)+1)
    result[st]=gate(i)
print(result)

    
