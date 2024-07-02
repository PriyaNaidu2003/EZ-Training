#hashing chaining

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class Hash:
    def __init__(self):
        self.Head=self.Tail=None

    def end_insertion(self, data):
        n = Node(data)
        if self.Head == None:
            self.Head = self.Tail = n
        else:
            self.Tail.next = n
            self.Tail = n
    def display(self):
        curr=self.Head
        if self.Head==None:
            print("None")
            return
        while curr!=None:
            print(curr.data,end=" ")
            curr=curr.next
        print()
    def search_key(self,ele,pos):
        curr=self.Head
        while curr!=None:
            if curr.data==ele:
                print(f"found at {pos}")
            curr=curr.next

        print("Not found")

k=list(map(int,input().split()))
n=len(k)
res=[None]*n
for i in range(n):
    res[i]=Hash()

for i in k:
    key=i%10
    res[key].end_insertion(i)

for i in res:

    i.display()
ele=int(input("enter element"))
pos=ele%10
res[pos].search_key(ele,pos)