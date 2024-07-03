# magic matrix 4X4:1 14 15 4 12 7 6 9 8 11 10 5 13 2 3 16
#magic matrix 3x3:9 2 7 4 6 8 5 10 3
import numpy as np
row=int(input("number of row"))
col=int(input("number of col"))

l=list(map(int,input().split()))
mat=np.array(l).reshape(row,col)
c=0

c_u=[0]
#check rows
for i in range(row):
    sum=0
    for j in range(col):


        sum+=mat[i][j]
        c_u[0]=sum
    if sum==c_u[0]:
        c+=1

#check colums
for i in range(row):
    sum=0
    for j in range(col):


        sum+=mat[j][i]
    if sum==c_u[0]:
        c+=1

#check diagonals
sum=0
for i in range(row):
    for j in range(col):

        if i==j:
            sum+=mat[i][j]
if sum==c_u[0]:
    c+=1

sum=0
j=0

for i in range(row):
   sum+=mat[i][row-j-1]

if sum==c_u[0]:
    c+=1
print(sum,c)
if c==(row+col+2):
    print("magic Square")
else:
    print("Not a magic square")