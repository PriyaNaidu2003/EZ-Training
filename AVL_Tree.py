#Balance_Factor=|LH-RH|<2

class node: #class to create a node
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        self.height=1
def ght(root):  #to calculate the height of the node
    if not root:
        return 0
    return root.height

def getBF(root):  #to calculate the balance factor of the node
    if not root:
        return 0
    return ght(root.left)-ght(root.right)
#Left Rotate
def leftRotate(A):
    B=A.right
    temp=B.left
    B.left=A
    A.right=temp

    A.height= 1 + max(ght(A.left), ght(A.right))
    B.height = 1 + max(ght(B.left), ght(B.right))

    return B


# Right Rotate
def rightRotate(A):
    B = A.left
    temp = B.right
    B.right= A
    A.left = temp

    A.height = 1 + max(ght(A.left), ght(A.right))
    B.height = 1 + max(ght(B.left), ght(B.right))

    return B



def insert(ele,root):       #inserting the elements into tree with balance factor
    if root==None:
        return node(ele)

    if ele<root.data:                   #binaery _search _tree type of insertion
        root.left=insert(ele,root.left)
    if ele>root.data:
        root.right=insert(ele,root.right)

    root.height=1+max(ght(root.left),ght(root.right)) #claculate height of each node
    BF=getBF(root) #get Balance factor for each node

    if BF>1 and ele<root.left.data:  #RR Rotation
        return rightRotate(root)

    if BF > 1 and ele > root.left.data:  #RL Rotation
        root.left=leftRotate(root.left)
        return rightRotate(root)

    if BF < -1 and ele > root.right.data:  # LL Rotation
        return leftRotate(root)

    if BF <-1  and ele < root.right.data:  # LR Rotation
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root

def inorder(root):#print the data in inorder format
    if root==None:
        return
    inorder(root.left)
    print(root.data,end=" ")

    inorder(root.right)
if __name__=="__main__":
    VL=[40,45,32,50,19,54,27,70,25,80,60,10,63,90]
    root = node((VL[0]))
    for i in VL[1:]:
        insert(i, root)
    inorder(root)