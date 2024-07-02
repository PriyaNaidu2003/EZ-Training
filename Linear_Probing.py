#first way
r=[22,10,47,56,100,50,92,99,79]
res=[False]*len(r)

for i in r:
    h_k=i%len(r)
    if res[h_k]==False:
        res[h_k]=i
    else:
        j=0
        h=h_k
        while res[h]!=False:
            j_k=(h_k+j)%10
            j+=1
            h=j_k


        res[j_k]=i
print(res)

#second way
k=[22,47,56,99,79]
res=[]
for i in range(len(k)):
    res[i]=False
for i in k:
    j=0
    j_key=i%len(k)
    while res[j_key]!=False and j<len(k):
        j_key=((i%10)+j)%len(k)
        j+=1
    res[j_key]=i

print(res)

