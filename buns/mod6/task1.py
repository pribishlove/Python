class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def push(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, index):
        if index < 0:
            return None
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current.data if current else None
    def remove(self, index):
        if index < 0:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                if current is None:
                    return
                current = current.next
            if current and current.next:
                current.next = current.next.next
    def insert(self, n, val):
        if n < 0:
            return
        new_node = Node(val)
        if n == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(n - 1):
                if current is None:
                    return
                current = current.next
            if current:
                new_node.next = current.next
                current.next = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

if __name__ == '__main__':
    linked_list = SinglyLinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    for value in linked_list:
        print(value)
    linked_list.insert(1, 4)
    for value in linked_list:
        print(value)
    linked_list.remove(2)
    for value in linked_list:
        print(value)