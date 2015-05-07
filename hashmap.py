__author__ = 'qiong'

# key is a string
# return an integer
def hash(key):
    return sum([ord(c) for c in key])

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

    # self node is the head of linkedlist and node to append to end
    def append(self, node):
        temp = self.next
        while temp:
            temp = temp.next
        temp.next = node

class HashMap:
    def __init__(self, n):
        if n<=0: raise ValueError
        self.capacity = n
        self.size = 0
        self.array = [None for i in range(n)]

    def get(self, key):
        idx = hash(key)%self.capacity
        for k, v in self.array[idx]:
            if k==key:
                return v
        return None

    def set(self, key, value):
        idx = hash(key)%self.capacity
        node = ListNode(key, value)
        if self.array[idx]==None:
            self.array[idx] = node
        else:
            # if node with the same key exists, update it
            temp = self.array[idx]
            while temp:
                if temp.key==key:
                    temp.value = value
                    break
                temp = temp.next
                self.size += 1
            temp.next = node

            if self.size>2*self.capacity:
                self.rehash(2*self.capacity)

    def delete(self, key):
        idx = hash(key)%self.capacity
        head = self.array[idx]
        self.remove(head, key)
        if self.size<self.capacity/2:
            self.rehash(self.capacity/2)

    def remove(self, head, key):
        if head:
            if head.key==key:
                self.head = self.head.next
            else:
                temp = head
                while temp.next:
                    if temp.next.key==key:
                        temp.next = temp.next.next
        return head


    def rehash(self, dest_capacity):
        result = [None for i in range(dest_capacity)]
        for node in self.array:
            temp = node
            while temp:
                idx = hash(temp.key)%dest_capacity
                if result[idx]==None:
                    result[idx]= node
                else:
                    result[idx].append(temp)

                temp = temp.next
        self.array = result