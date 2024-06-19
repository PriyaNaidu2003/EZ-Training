def max_sum(k,lst):
    window=max=0
    window=sum(lst[:k])   #window
    for i in range(1,len(lst)-(k-1)):
        if max<window:
            max=window
            pos=i
        window=window-lst[i-1]+lst[i+k-1]      #slider
    result=lst[pos:pos+k]
    return result

k=int(input("Enter the nomber of continuous inputs: "))
#lst=list(map(int,input().split()))
lst=[2,4,3,5]#,6,3,4,6,7,1,2,5]
print(max_sum(k,lst)) 
