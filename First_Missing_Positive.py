nums=list(map(int,input().split()))
nums.sort()
c=1
for i in nums:
    if c==i:
        c+=1
print(c)