#Bubble_sort
lst=list(map(int,input().split()))
for j in range(0,len(lst)):
    for i in range(0,len(lst)-1-j):
        if lst[i]>lst[i+1]:
            lst[i],lst[i+1]=lst[i+1],lst[i]
print(lst)


#Selection_sort.py

lst=list(map(int,input().split()))

for i in range(len(lst)):
    min = lst[i]
    pos = i
    for j in range(i,len(lst)):
        if min > lst[j]:
            min=lst[j]
            pos=j
    lst[i],lst[pos]=lst[pos],lst[i]
print(lst)


#Insertion Sort

def insertionSort(arr):
    n = len(arr)  

    if n <= 1:
        return  

    for i in range(1, n):  
        key = arr[i] 
        j = i - 1
        while j >= 0 and key < arr[j]:  
            arr[j + 1] = arr[j] 
            j -= 1
        arr[j + 1] = key  



if __name__=="__main__":
    lst=list(map(int,input().split()))
    insertionSort(lst)
    print(lst)



# Quick_sort

def partition(lst,Low,High):
    pivot = lst[High]
    j=Low-1
    for i in range(Low, High):
        if lst[i] <= pivot:
            j+=1
            lst[j],lst[i]=lst[i],lst[j]
    j+=1
    lst[j], lst[High] = lst[High], lst[j]
    pi=j
    return pi
def quick_sort(lst,low,high):
    if low<high:
        pi=partition(lst,low,high)
        quick_sort(lst,low,pi-1)
        quick_sort(lst,pi+1,high)


if __name__=="__main__":
    lst=list(map(int,input().split()))
    quick_sort(lst,0,len(lst)-1)
    print(lst)

#Merge_sort

def merge(lst,low,mid,high):
    left=lst[low:mid+1]
    right=lst[mid+1:high+1]

    i=j=0
    t=low


    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            lst[t]=left[i]
            t+=1
            i+=1
        elif left[i]>right[j]:
            lst[t] = right[j]
            t += 1
            j += 1
    while i<len(left):
        lst[t] = left[i]
        t += 1
        i += 1
    while j < len(right):
        lst[t] = right[j]
        t += 1
        j += 1

def merge_sort(lst,low,high):
    if low<high:
        mid=low+(high-low)//2
        merge_sort(lst,low,mid)
        merge_sort(lst,mid+1,high)

        merge(lst,low,mid,high)

if __name__=="__main__":
    lst=list(map(int,input().split()))
    merge_sort(lst,0,len(lst)-1)
    print(lst)
