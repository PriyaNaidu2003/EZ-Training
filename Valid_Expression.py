class stack:
    def __init__(self):
        self.items=[]
    def push(self,b):
        self.items.append(b)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

s=stack()
exp=input()
flag=True
for i in exp:
    if i =="(" or i=="{" or i=="[":
        s.push(i)
    elif i ==")" or i=="}" or i=="]":
        r=s.pop()
        if (i==")" and r!="(") or (i=="}" and r!="{") or (i=="]" and r!="["):
            flag=False
            break

if flag and s.size()==0:
    print("valid")
else:
    print("Invalid")
