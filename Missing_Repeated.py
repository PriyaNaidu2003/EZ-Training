# leetcode Find Misssing and Repeating values
#using dictionary (optimal solution)
# n=int(input())
# a=[]
# l=[]
# d={}
# for i in range(0,n):
#     sub=[]
#     for j in range(0,n):
#         ele=int(input())
#         sub.append(ele)
#     a.append(sub)
# for i in a:
#     for j in i:
#         if j not in d:
#             d[j]=1
#         else:
#
#             l.append(j)
#
# for i in range(1,(n**2)+1):
#     if i not in d:
#         l.append(i)
# print(l)


#using list

n=int(input())
a=[]
l=[]
d=[0]*n*n
print(d)
for i in range(0,n):
    sub=[]
    for j in range(0,n):
        ele=int(input())
        sub.append(ele)
    a.append(sub)
for i in a:
    for j in i:
        if d[j-1]==0:
            d[j-1]+=1
        else:

            l.append(j)



for i in range(len(d)):
    if d[i]==0:
        l.append(i+1)
print(l)






