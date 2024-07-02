# class Node:
#     def __init__(self,data):
#         self.value=data
#         self.next=None
# Head=Tail=Node(10)
#
# Tail.next=Node(20)
# Tail=Tail.next
#
# Tail.next=Node(30)
# Tail=Tail.next

class Node:
    def __init__(self,data):
        self.value=data
        self.next=None
class Link_list:
    def __init__(self):
        self.Head=self.Tail=None
    def front_insertion(self,data):
        n=Node(data)
        if self.Head==None:
            self.Head=self.Tail=n
        else:
            n.next=self.Head
            self.Head=n

    def end_insertion(self,data):
        n = Node(data)
        if self.Head == None:
            self.Head =self.Tail= n
        else:
            self.Tail.next=n
            self.Tail=n

    def At_pos(self, data,pos):
        n = Node(data)
        if self.Head == None:
            self.Head =self.Tail= n
        else:
            curr=self.Head
            count=0
            while curr!=None and count<pos-1:
                curr=curr.next
                count+=1

            n.next = curr.next
            curr.next = n

    def display(self):
        curr=self.Head
        while curr!=None:
            print(curr.value)
            curr=curr.next
    def Front_deletion(self):
        if self.Head == None:
            print("list is empty")

        curr=self.Head
        self.Head=self.Head.next
        curr.next=None
    def End_deletion(self):
        curr=self.Head
        while curr.next!=self.Tail:
            curr=curr.next
        curr.next=None
        self.Tail=curr
    def find(self,key):
        curr=self.Head
        index=0
        while curr!=None:
            if curr.value==key:
                return index
            else:
                curr=curr.next
                index+=1





    def Del_Pos(self,pos):


        if self.Head == None:
            print('list is empty')
        else:
            curr = self.Head
            prev = self.Head
            count = 0
            while pos!=count:
                count += 1
                prev=curr
                curr = curr.next


            prev.next=curr.next



l=Link_list()

l.front_insertion(20)
l.end_insertion(30)
l.front_insertion(10)
l.At_pos(15,1)

l.display()
v=l.find(15)
if v!=None:
    print(v)
else:
    print("element not found")
print("--------------")
l.Front_deletion()
l.display()
print("--------------")
l.End_deletion()
l.display()
print("--------------")
l.front_insertion(5)
l.Del_Pos(1)
l.display()








