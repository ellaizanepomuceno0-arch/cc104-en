# m45doublelinklist.py

class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):  
        new_node = DNode(data)

        if self.head:
            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node

    def traverse_forward(self):  
        current = self.head

        while current:
            print(current.data, end=" <-> ")
            current = current.next

        print("None")


if __name__ == "__main__":
    doubly_list = DoublyLinkedList()

    doubly_list.insert_at_head(10)
    doubly_list.insert_at_head(20)
    doubly_list.insert_at_head(30)

    print("Doubly Linked List (Forward):")
    doubly_list.traverse_forward()
