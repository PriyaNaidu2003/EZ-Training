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
vals=input()
s=Stack()
flag=0
brackets=['{','[','(']
brrack=['}',']',')']
for i in vals:
    if i in brackets:
        s.push(i)
    elif i in brrack:
        p=s.pop()
        if (i==')' and '(' !=p) or (i=='}' and '{' !=p) or (i==']' and '[' !=p):
            flag=1



if  flag==0 and s.size()==0:
    print('valid')
else:
    print('invalid')


# class Stack:
#     def __init__(self):
#         self.items=[]
#     def push(self,data):
#         self.items.append(data)
#     def pop(self):
#         return self.items.pop()
#     def size(self):
#         size=len(self.items)
#         return size
# vals=input()
# s=Stack()
# flag=True
# brackets=['{','[','(']
# brrack=['}',']',')']
# d={')':'(','}':'{',']':'['}
# for i in vals:
#     if i in brackets:
#         s.push(i)
#     elif i in brrack:
#         p=s.pop()
#
#         if d[i]==p:
#             flag=False
#             break
#
#
# if flag:
#     print('valid')
# else:
#     print('invalid')




