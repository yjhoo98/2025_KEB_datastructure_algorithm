import sys
class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None
def insert(root,value):
    if root is None:
        node = TreeNode()
        node.data = value
        return node
    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root
def search(root,value):
    current = root
    while True:
        if value == current.data:
            return current
        elif value < current.data:
            current = current.left
        else:
            current = current.right
    return None
def delete(root,value):
    if root is None:
        return root
    if value<root.data:
        root.left=delete(root.left,value)
    elif value>root.data:
        root.right=delete(root.right,value)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            root.data=min_value(root.right).data
            root.right=delete(root.right,value)
    return root
def min_value(node):
    current=node
    while current.left is not None:
        current=current.left
    return current
def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(f'{node.data} ',end='')
def josephus(node,k):
    return node
if __name__ == "__main__":
    n,k=map(int,sys.stdin.readline().split())
    root=None
    for i in range(n,0,-1):
        root = insert(root, i)
