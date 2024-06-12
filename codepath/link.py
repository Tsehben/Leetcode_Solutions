class Node:
    def __init__(self, data = None, next= None):
        self.data = data 
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_list(self):
        if self.head is None:
            print("Linked List is empty")
            return 
        
        itr = self.head
        llitr = ""
        while itr:
            llitr += str(itr.data) + ("-->" if itr.next else "")
            itr = itr.next

        print(llitr)
        return
    

ll = LinkedList()

ll.insert_at_beginning(3)
ll.insert_at_beginning(10)
ll.insert_at_beginning(9)
ll.insert_at_beginning(7)
ll.insert_at_beginning(6)
ll.print_list()
