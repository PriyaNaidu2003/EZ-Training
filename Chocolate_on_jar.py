chocolate=list(map(int,input().split()))
jar=int(input())
A=0
for i in chocolate:
    A=A+i//3
    if i%3:
        A+=1
print(A)
