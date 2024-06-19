n=int(input())
k=int(input())
d=list(map(int,input().split()))
max=-1

for i in range(len(d)-(k-1)):
    blank=[]
    total=0
    for m in range(k):
        blank.append(d[i+m])
    #temp=d[i:i+k]
    for j in range(len(blank)):
        total+=blank[j]*(j+1)

        if total>max:
            max=total
print(max)
