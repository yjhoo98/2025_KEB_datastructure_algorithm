class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None
def insert_tree(root,node,value=[]):

    node.data = value[0]
    for value in value[1:]:
        node = TreeNode()
        node.data = value
        current = root
        while True:
            if value < current.data:
                if current.left is None:
                    current.left = node
                    break
                current = current.left  # move
            else:
                if current.right is None:
                    current.right = node
                    break
                current = current.right  # move
    print("complete binary search tree")
def search_value(root,value):
    current=root
    while True:
        if value == current.data:
            print(f'{value}을(를) 찾았습니다.')
            break
        elif value < current.data:
            if current.left is None:
                print(f"{value}이(가) 존재하지 않습니다.")
                break
            current = current.left
        else:
            if current.right is None:
                print(f"{value}이(가) 존재하지 않습니다.")
                break
            current = current.right

def delete_value(root,value):
    current=root
    parent = None
    parent = root
    while True:
        if value == current.data:
            if current.left is None and current.right is None:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
                del (current)
            elif current.left is not None and current.right is None:
                if parent.left == current:
                    parent.left = current.left
                else:
                    parent.right = current.left
                del (current)
            elif current.left is None and current.right is not None:
                if parent.left == current:
                    parent.left = current.right
                else:
                    parent.right = current.right
                del (current)
            elif current.left is not None and current.right is not None:
                pass
            print(f"{value}이(가) 삭제됨.")
            break
        elif value < current.data:
            if current.left is None:
                print(f'{value}이(가) 없음')
                break
            parent = current
            current = current.left
        else:
            if current.right is None:
                print(f'{value}이(가) 없음')
                break
            parent = current
            current = current.right
if __name__=="__main__":
    groups=['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']
    root=None
    node=TreeNode()
    root=node
    insert_tree(root,node,groups)
    find_group=input()
    search_value(root,find_group)
    deleteName=input()
    delete_value(root,deleteName)
