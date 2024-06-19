#012 sort
lis=[2,1,0,1,1,2,0,0]
countz=0
counto=0
countt=0

for j in range(len(lis)):
    if(lis[j]==0):
        countz+=1
    elif lis[j]==1:
        counto+=1
    else:
        countt+=1
j=0
while countz>0:
    lis[j]=0
    j+=1
    countz-=1
while counto>0:
    lis[j]=1
    j+=1
    counto-=1
while countt>0:
    lis[j]=2
    j+=1
    countt-=1
print(lis)
