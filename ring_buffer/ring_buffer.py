from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Current tracks the LRU item in each batch
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            removed_node = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if removed_node == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        list_buffer_contents.append(self.current.value)

        if self.current == self.storage.tail:
            node = self.storage.head
        else:
            node = self.current.next

        while node is not self.current:
            list_buffer_contents.append(node.value)
            node = node.next if node.next else self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = -1
        self.storage = [None] * capacity

    def append(self, item):
        self.current += 1
        if self.current > len(self.storage) - 1:
            self.current = 0
        self.storage[self.current] = item

    def get(self):
        return [x for x in self.storage if x is not None]


a = RingBuffer(3)
a.append('a')
a.append('b')
a.append('c')
a.append('d')
a.append('e')
a.append('f')

print(a.storage.head.value)
print(a.storage.tail.value)
