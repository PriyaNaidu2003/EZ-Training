x=[2,4,6,8,10,11]
y=[3,5,7,9,10,12]
filter_list=[]
for i in x:
    if i not in y and i%2==0:
        filter_list.append(i)
print(filter_list)


filter_list=[i for i in x if i not in y and i%2==0]
print(filter_list)


num=[1,2,3,4,5,6,7,8,9]
list2=[]
for i in num:
    if i%2==0:
        list2.append(i**2)
print(list2)
