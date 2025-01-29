class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def built(self, data_list):
        self.head = None
        for data in data_list[::-1]:
            self.head, self.head.next = Node(data), self.head

    def size(self):
        return sum(1 for _ in self)

    def __len__(self):
        return self.size()

    def get_at(self, index):
        return (current := self.head) and (current := current.next) if index > 0 else current.data

    def set_at(self, index, value):
        if (current := self.head) and (current := current.next) if index > 0 else current:
            current.data = value

    def get_first(self):
        return self.get_at(0)

    def get_last(self):
        return self.get_at(self.size() - 1)

    def set_first(self, value):
        self.set_at(0, value)

    def set_last(self, value):
        self.set_at(self.size() - 1, value)

    def insert(self, data, index):
        if index < 0 or index > self.size():
            return None
        self.head, self.head.next = (new_node := Node(data)), self.head if index == 0 else new_node, self.head.next

    def insert_first(self, data):
        self.insert(data, 0)

    def insert_last(self, data):
        self.insert(data, self.size())

    def delete(self, index):
        if index < 0 or index >= self.size():
            return None
        deleted_value, self.head = self.head.data, self.head.next if index == 0 else self.head, self.head.next.next
        return deleted_value

    def delete_first(self):
        return self.delete(0)

    def delete_last(self):
        return self.delete(self.size() - 1)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def display(self):
        print(" -> ".join(str(current.data) for current in self))


# Example usage:
linked_list = LinkedList()
linked_list.built([1, 2, 3, 4, 5])

print("Linked List:")
linked_list.display()
print(f"Length: {len(linked_list)}")

print(f"Get at index 2: {linked_list.get_at(2)}")
linked_list.set_at(2, 10)
print("After setting at index 2 to 10:")
linked_list.display()

print(f"Get first element: {linked_list.get_first()}")
print(f"Get last element: {linked_list.get_last()}")

linked_list.set_first(100)
linked_list.set_last(200)
print("After setting first to 100 and last to 200:")
linked_list.display()

linked_list.insert_first(0)
linked_list.insert_last(300)
linked_list.insert(99, 2)
print("After inserting 0 at first, 300 at last, and 99 at index 2:")
linked_list.display()

deleted_value = linked_list.delete_first()
print(f"Deleted first element, value: {deleted_value}")
linked_list.display()

deleted_value = linked_list.delete_last()
print(f"Deleted last element, value: {deleted_value}")
linked_list.display()

deleted_value = linked_list.delete(1)
print(f"Deleted element at index 1, value: {deleted_value}")
linked_list.display()
