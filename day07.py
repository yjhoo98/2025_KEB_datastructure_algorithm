import random
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        if not self.head:
            self.head=Node(data)
            return
        current=self.head
        while current.next:#if next node exist
            current=current.next#move
        current.next=Node(data)
    def search(self,target):
        current=self.head
        while current.next:
            if current.data==target:
                return True
            else:
                current=current.next
        return False
    def __str__(self):
        node=self.head
        while node is not None:
            print(node.data)
            node=node.next
        return "end"
if __name__=="__main__":
    l=LinkedList()
    i=0
    while i<20:
        n=random.randint(1,20)
        l.append(n)
        print(n,end=' ')
        i=i+1
    print(l.search(10))