class node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
class node_data:
    def __init__(self,node,hkey):
        self.node=node
        self.hkey=hkey
def top_view(root):
    temp=node_data(root,0)
    q=[temp]
    q.append(None)

    key_dict={}
    while (len(q) > 0):
        curr = q.pop(0)
        if curr == None:
            if len(q) == 0:
                break
            else:
                q.append(None)
        else:
            if curr.hkey not in key_dict.keys():
                key_dict[curr.hkey]=curr.node.data
            if curr.node.left != None:
                temp=node_data(curr.node.left,curr.hkey-1)
                q.append(temp)
            if curr.node.right != None:
                temp=node_data(curr.node.right,curr.hkey+1)
                q.append(temp)

    for i in sorted(key_dict):
        print(key_dict[i],end=" ")


def bottom_view(root):
    temp = node_data(root, 0)
    q = [temp]
    q.append(None)

    key_dict = {}
    while (len(q) > 0):
        curr = q.pop(0)
        if curr == None:
            if len(q) == 0:
                break
            else:
                q.append(None)
        else:
            key_dict[curr.hkey] = curr.node.data
            if curr.node.left != None:
                temp = node_data(curr.node.left, curr.hkey - 1)
                q.append(temp)
            if curr.node.right != None:
                temp = node_data(curr.node.right, curr.hkey + 1)
                q.append(temp)

    for i in sorted(key_dict):
        print(key_dict[i],end=" ")


def left_view(root):

    q = [root]
    q.append(None)
    print(root.data,end=" ")
    while (len(q) > 0):
        curr = q.pop(0)
        if curr == None:
            if len(q) == 0:
                break
            else:

                print(q[0].data, end=" ")
                q.append(None)
        else:

            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)

def right_view(root):
    q = [root]
    q.append(None)
    while (len(q) > 0):
        curr = q.pop(0)
        if curr == None:
            if len(q) == 0:
                break
            else:


                q.append(None)
        else:
            if q[0]==None:
                print(curr.data,end=" ")

            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)


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

    print("Top view nodes")
    top_view(root)
    print()
    print("Bottom view nodes")
    bottom_view(root)
    print()
    print("Left view nodes")
    left_view(root)
    print()
    print("Right view nodes")
    right_view(root)
