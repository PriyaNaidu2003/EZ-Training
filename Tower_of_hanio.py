c=[0]
def Tower(n,sr,dest,temp,c):
    if n==0:
        return

    Tower(n-1,sr,temp,dest,c)
    print(f"move {n}th from {sr} to {dest}")
    c[0]+=1
    Tower(n-1,temp,dest,sr,c)
Tower(4,'A','C','B',c)
print(c)