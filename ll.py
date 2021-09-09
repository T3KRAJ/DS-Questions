class Node:
    def __init__(self, data=None):
        self.value = data
        self.ref = None
class Linked_List:
    def __init__(self, data=None):
        self.start_node = Node(data)

    def append_at_head(self, data):
        self.head = Node(data)
        self.head.ref = self.start_node
        self.start_node = self.head

    def append(self, data):
        self.part = Node(data)
        current = self.start_node
        if current:
            while current.ref:
                current = current.ref
            current.ref = self.part
        else:
             current = self.part
    
    def insert_at_certain_position(self, pos, data):
        self.part = Node(data)
        current = self.start_node
        try:
            for _ in range(pos-1):
                current = current.ref
            self.part.ref = current.ref
            current.ref = self.part
        except:
            print('Position not found')

    def delete_at_certain_position(self, pos):
        current = self.start_node
        try:
            for _ in range(pos-1):
                current = current.ref
            current.ref = current.ref.ref
        except:
            print('Position not found')
        
    
    def length(self):
        current = self.start_node
        if not current:
            return (0)
        count = 1
        while current.ref:
            count += 1
            current = current.ref
        return count
        
    
    def traverse(self):
        current = self.start_node
        while current:
            print(current.value)
            current = current.ref




#head node
ll = Linked_List(3) 
ll.append(7)
ll.append(5)
ll.append(8)

ll.append_at_head(0)
ll.append_at_head(2)

#position starting from '0'
ll.insert_at_certain_position(2, 10)

print(ll.length())
print('******')

ll.traverse()
print('******')

#position starting from '0'
ll.delete_at_certain_position(7)
ll.traverse()