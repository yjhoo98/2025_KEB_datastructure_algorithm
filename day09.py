class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None
def insert(root,value):
    if root is None:
        node=TreeNode()
        node.data=value
        return node
    if value<root.data:
        root.left=insert(root.left,value)
    else:
        root.right=insert(root.right,value)
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

if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None
    for number in numbers:
        root=insert(root,number)
    print("BST 구성 완료")
    post_order(root)
    print()
    # find_number = int(input())
    # if search(root,find_number):
    #     print(f'{find_number} 발견')
    # else:
    #     print(f'{find_number} 발견 x')
    d_number = int(input())
    if search(root,d_number):
        root=delete(root,d_number)
    else:
        print(f'not exist')
    post_order(root)