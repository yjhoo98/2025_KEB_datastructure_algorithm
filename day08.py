
class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None

if __name__=="__main__":
    groups=['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']
    # groups=[10,15,8,3,9]
    root=None
    node=TreeNode()
    node.data=groups[0]
    root = node
    for groups in groups[1:]:
        node=TreeNode()
        node.data=groups
        current=root
        while True:
            if groups<current.data:
                if current.left is None:
                    current.left=node
                    break
                current=current.left # move
            else:
                if current.right is None:
                    current.right=node
                    break
                current=current.right # move
    print("complete binary search tree")
    find_group=input()
    current=root
    while True:
        if find_group==current.data:
            print(f'{find_group}을(를) 찾았습니다.')
            break
        elif find_group<current.data:
            if current.left is None:
                print(f"{find_group}이(가) 존재하지 않습니다.")
                break
            current=current.left
        else:
            if current.right is None:
                print(f"{find_group}이(가) 존재하지 않습니다.")
                break
            current=current.right

    deleteName=input()
    parent=None
    parent=root
    while True:
        if deleteName==current.data:
            if current.left is None and current.right is None:
                if parent.left==current:
                    parent.left=None
                else:
                    parent.right=None
                del(current)
            elif current.left is not None and current.right is None:
                if parent.left==current:
                    parent.left=current.left
                else:
                    parent.right=current.left
                del(current)
            elif current.left is None and current.right is not None:
                if parent.left==current:
                    parent.left=current.right
                else:
                    parent.right=current.left
                del(current)
            print(f"{deleteName}이(가) 삭제됨.")
            break
        elif deleteName<current.data:
            if current.left is None:
                print(f'{deleteName}이(가) 없음')
                break
            parent=current
            current=current.left
        else:
            if current.right is None:
                print(f'{deleteName}이(가) 없음')
                break
            parent=current
            current=current.right
