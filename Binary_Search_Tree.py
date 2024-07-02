class node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
class Queue:
    def __init__(self):
        self.item=[]
    def push(self,data):
        self.item.append(data)
    def pop(self):
        return self.item.pop(0)
    def size(self):
        return len(self.item)

# def binary_search(ele,root):
#     curr=node(ele)
#     if curr.data<root.data:
#         if root.left==None:     #base case
#             root.left=curr
#         else:
#             binary_search(ele,root.left)
#     elif curr.data>root.data:
#         if root.right==None:        #base case
#             root.right=curr
#         else:
#             binary_search(ele,root.right)
#     else:
#         return
#2nd way of binary search
def binary_search(ele,root):
    if root==None:
        return node(ele)

    if ele<root.data:
        root.left=binary_search(ele,root.left)
    if ele>root.data:
        root.right=binary_search(ele,root.right)

    return root


def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.data,end=" ")

    inorder(root.right)


def preorder(root):
    if root == None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

def postorder(root):

    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")
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
    lst=[4,6,7,3,8,2,5,9,1]
    root=node((lst[0]))
    for i in lst[1:]:
        binary_search(i,root)

    print("preorder")
    preorder(root)
    print()
    print("inorder")
    inorder(root)
    print()
    print("postorder")
    postorder(root)
    print()
    print("Level order")
    level_order(root)
    print()
    print("Height of the tree")
    print(height(root))
    print()
    print("leaf nodes")
    leaf_nodes(root)






