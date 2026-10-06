# m45singlelinklist.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):  
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):  
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def traverse(self):  
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


if __name__ == "__main__":
    linked_list = SinglyLinkedList()

    linked_list.insert_at_head(10)
    linked_list.insert_at_head(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(40)

    print("Singly Linked List:")
    linked_list.traverse()

 