cards=list(map(int,input().split()))
min=999
f=False
for i in range(len(cards)):
    s=0
    for j in range(i+1,len(cards)):
        if cards[i]==cards[j]:
            s=j-i+1
            if min>s:
                min=s
                f=True
if f:
    print(min)
else:
    print(-1)


# m=999
# dic={}
# for i,c in enumerate(cards):
#     if c in dic:
#         m=min(m,i-dic[i]+1)
#     dic[c]=i
# if m!=999:
#     print(m)
# else:
#     print(-1)
