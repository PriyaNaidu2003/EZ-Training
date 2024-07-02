P=[5,10,15,7,8,9,4]
W=[1,3,5,4,1,3,2]

P_W={}
for i in range(len(P)):
    P_W[i]=P[i]/W[i]
l=list(P_W.items())
#l.sort(key=lambda x:x[1],reverse=True)
sorted_list=sorted(l,key=lambda x:x[1],reverse=True)