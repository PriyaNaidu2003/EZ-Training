n=int(input())
peaks=list(map(int,input().split()))

max=0
for k in range(1,len(peaks)-1):
    i=k-1
    j=k+1
    if peaks[k]>peaks[i] and peaks[k]>peaks[j]:
        if peaks[k]>max:
            max=peaks[k]
            ans=k

print(ans)
