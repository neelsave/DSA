class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
        
# function to insert a node
def insert(root,node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right,node)
        else:
            if root.val > node.val:
                if root.left is None:
                    root.left = node
                else:
                    insert(root.left,node)
        
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
        
# A utility function to search a given  key in BST        
def search(root,key):
    
    # Base cases: root is null or key is present at root
    if root is None or root.val == key:
        return root
    
    #key is greater than root key
    if root.val < key:
        return search(root.right,key)
    
    #if key is smaller than the root key
    return search(root.left,key)
        
        
# Driver program to test the above functions 
# Let us create the following BST 
#       50 
#     /   \ 
#   30    70 
#   / \   / \ 
#  20 40 60 80
        
r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))

inorder(r)

print(search(r,30))