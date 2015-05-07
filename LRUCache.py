__author__ = 'qiong'
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_end(self, node):
        if self.head==None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def remove(self, node):

        if node==self.head:
            self.head = self.head.next
            self.head.prev = None
        if node==self.tail:
            temp = self.tail.prev
            self.tail = temp
            self.tail.next = None
        temp = self.head.next
        while temp != self.tail:
             if temp==node:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev

    def remove_h(self):
        if self.head!=self.tail:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
            self.tail = None

    def move_to_end(self, node):
        if self.head == node:
            if self.tail != self.head:
                temp = self.head
                self.head = self.head.next
                self.head.prev = None
                self.add_to_end(node)
        elif self.tail == node:
            return
        else:
            temp = self.head
            while temp != self.tail:
                if temp == node:
                    temp.next.prev = temp.prev
                    temp.prev.next = temp.next
            self.add_to_end(node)

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = {} # value is listNode
        self.size = 0
        self.list = DoubleLinkedList()

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.dict:
            # key found in current cache, then update the value and move node to tail
            node = self.dict[key]
            node.value = value
            self.list.move_to_end(node)
        else:
            # key not found in current cache, first add node, then check for capacity
            node = ListNode(key, value)
            self.dict[key] = node
            self.list.add_to_end(node)
            if self.size>=self.capacity:
            # delete head node when reaches capacity
                node = self.list.remove_h()

    # return an integer
    def get(self, key):
        if key in self.dict:
            node = self.dict[key]
            self.list.move_to_end()
            return node.value
        return None

    def delete(self, key):
        if key in self.dict:
            node = self.dict[key]
            self.list.remove(node)
            del self.dict[key]
        else:
            raise KeyError