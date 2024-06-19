#Depth first search - preorder,inoder,postorder

class node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
#Queue is used in Breadth first search-Level order
class Queue:
    def __init__(self):
        self.item=[]
    def push(self,data):
        self.item.append(data)
    def pop(self):
        return self.item.pop(0)
    def size(self):
        return len(self.item)

def preorder(root):
    if root==None:
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.data,end=" ")

    inorder(root.right)



def postorder(root):

    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")

#Breadth first search-Level order
def level_order(root) :
    q=Queue()
    q.push(root)
    q.push(None)
    while(q.size()>0):
        curr=q.pop()
        if curr==None:
            if q.size()==0:
                break
            else:
                print()
                q.push(None)
        else:
            print(curr.data,end=" ")
            if curr.left!=None:
                q.push(curr.left)
            if curr.right != None:
                q.push(curr.right)
def height(root):
    if root==None:
        return 0
    LH=height(root.left)
    RH=height(root.right)
    return max(LH,RH)+1
def leaf_nodes(root):
    if root==None:
        return
    if root.left==None and root.right==None:
        print(root.data,end=" ")
    leaf_nodes(root.left)
    leaf_nodes(root.right)



if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(3)
    root.left.left=node(4)
    root.left.right=node(5)
    root.right.left = node(6)
    root.right.right = node(7)
    root.left.right.left = node(8)
    root.left.right.right = node(9)
    root.right.right.right= node(10)
    root.left.right.right.left = node(11)
    root.left.right.right.right = node(12)

    print("preorder")
    preorder(root)
    print("\ninorder")
    inorder(root)
    
    print("\npostorder")
    postorder(root)
    
    print("\nLevel order")
    level_order(root)
    
    print("\nHeight of the tree")
    print(height(root))
    
    print("\nleaf nodes")
    leaf_nodes(root)
