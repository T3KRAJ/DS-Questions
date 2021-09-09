class Node:
    def __init__(self, data=None):
        self.value = data
        self.ref = None

class Linked_List:
    def __init__(self, data=None):
        self.start_node = Node(data)

    def insert(self, data):
        current = self.start_node
        if current is not None:
            while current.ref:
                current = current.ref
            current.ref = Node(data)
        else:
            self.start_node = Node(data)
            print(current.value)
    
    def delete(self):
        current = self.start_node
        if current: 
            while current:
                current = current.ref
    def traverse(self):
        current = self.start_node
        if current is not None:
            while current:
                current = current.ref


def push(data):
    obj = Linked_List()
    obj.insert(data)

def pop():
    obj = Linked_List()
    obj.delete()

def traverse():
    obj = Linked_List()
    obj.traverse()

push(2)
traverse()