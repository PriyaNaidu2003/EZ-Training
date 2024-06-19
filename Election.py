'''def vote_count(vote):
   c={}
    win=[]
    for i in vote:
        if i not in c:
            c[i]=vote.count(i)
    m=max(c.values())
    for i in c:
        if c[i]==m:
            win.append(i)
    if len(win)>1:
        print(-1)
        return win
    else:
        return win[0]
    
    '''
def vote_count(vote):
    count=[0]*6
    for i in vote:
        count[i-1]+=1
    return (count.index(max(count))+1)

vote=list(map(int,input().split()))
print(vote_count(vote))
