class Stack:
    def __init__(self):
        self.items=[]
        self.items.append(-1)
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def size(self):
        size=len(self.items)
        return size
    def top(self):
        return self.items[-1]

s=Stack()

lis=[14,2,16,4,2,5]

o=[0]*len(lis)
for i in range(len(lis)-1,-1,-1):
    if s.size()!=0:
        while s.size()!=0 and s.top()<=lis[i]:
            if s.top()<=lis[i]:
                s.pop()
    if s.size()==0:
        o[i]=-1
    else:
        o[i]=s.top()
    s.push(lis[i])
print(o)
