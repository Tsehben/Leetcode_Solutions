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
    
    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        node = Node(data, None)
        itr.next = node
        return 
    
    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)
        

    def get_length(self):
        count = 0

        if self.head is None:
            print(count)
            return 
        
        count = 1
        itr = self.head
        while itr.next:
            count += 1
            itr = itr.next
        

        return count
        
    def remove(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

        return
    
    def insert(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
    
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)

              
                
                break
            
            itr = itr.next
            count += 1
        return

    


    

ll = LinkedList()

ll.insert_at_beginning(3)
ll.insert_at_beginning(10)
ll.insert_at_beginning(9)
ll.insert_at_beginning(7)
ll.insert_at_beginning(6)
ll.insert_at_end(89)
ll.insert_at_end(80)
# ll.insert_values(["Eben","Kwaku", "Tseh"])


#ll.get_length()
# ll.remove(2)
# ll.remove(4)
ll.insert(3,12)
ll.print_list()