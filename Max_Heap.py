def max_heap(l):

    while i>1:
        if l[i]>l[i//2]:
            l[i],l[i//2]=l[i//2],l[i]
        else:
            break

l=[3,2,4,6,1,5,8]
max_heap(l)
print(l)
