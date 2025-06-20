'''class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)

def preorder(root):
    if root is None:
        return
    else:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
preorder(root)'''


'''class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)

def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
inorder(root)'''


'''class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)

def postorder(root):
    if root is None:
        return
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
postorder(root)'''

'''class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)
def height(root):
    if root is None:
        return 0
    else:
        return max(height(root.left), height(root.right))+1
print('The height is:',height(root))'''


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)

def countleaf(root):
    if root is None:
        return 0
    if root is not None and root.left is None and root.right is None:
        return 1
    else:
        return countleaf(root.left) + countleaf(root.right)
print('The count is:',countleaf(root))
    
    
    

