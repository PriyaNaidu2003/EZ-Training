pizza,frds=map(int,input().split())
num=frds+1
sum=0
while True:
    if pizza%num!=0:
        num+=1
    else:
        while num>0:
            rem=num%10
            sum+=rem
            num//=10
        break
print(sum)
