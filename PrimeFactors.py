n=int(input())
vals=list(map(int,input().split()))
pr_num=int(input())
d={}
sum=0
i=2
while i<=pr_num:
    if pr_num%i==0:

        pr_num = pr_num // i
    else:
        i=i+1

    if i  not in d:
        d[i]=1
    else:
        d[i]+=1

for i,j in d.items():
    sum=sum+j*vals[i]
print(sum)
