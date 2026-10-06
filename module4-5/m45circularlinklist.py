class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):  
        new_node = CNode(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def traverse(self): 
        if not self.head:
            print("List is empty.")
            return

        current = self.head

        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(back to head)")

if __name__ == "__main__":
    circular_list = CircularLinkedList()

    circular_list.insert(10)
    circular_list.insert(20)
    circular_list.insert(30)
    circular_list.insert(40)

    print("Circular Linked List:")
    circular_list.traverse()
