n=int(input())
c=1000
comma=1
res=0
while c<=n:
    m=c*1000
    num=min(n-c+1,m-c)
    res=num*comma
    c=m
    comma+=1
print(res)


