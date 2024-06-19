def vol_rep(s):
    vol=['a','e','i','o','u']
    count={}
    for i in vol:
        count[i]=s.count(i)
    m=max(count.values())
    for i in count:
        if count[i]==m:
            r=i
            break
    return r 

s=input()
print(vol_rep(s))







def dog_age(n):
    return n*7
n=int(input())
print(dog_age(n))
