__author__ = 'qiong'

# epi 4.11
# start time 8:55 pm
# initial trial end time 10:15 pm
# initial trial time complexity O(n^2)
# space complexity O(1)? recursive O(n)?

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def zip_list(head):
    if not head:
        return None
    n = 0
    l1 = head
    while l1:
        n += 1
        l1 = l1.next

    return zip_list_helper(head, n)

def zip_list_helper(head, n):
    print 'entering helper with n=%d'%n
    if n==1 or n==2:
        return head
    l1 = head.next
    if n==3:
        head.next = l1.next
        head.next.next = l1
        l1.next = None
        return head

    l2 = head.next
    r1 = head
    r2 = None
    count = n
    while count>2:
        r1 = r1.next
        count -= 1
    print 'r1=%d'%r1.val
    r2 = r1.next
    r1.next = None
    l1.next = r2
    r2.next = l2
    l2 = zip_list_helper(l2, n-2)
    return head

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
zip_list(a)
temp = a
while temp:
    print temp.val
    temp = temp.next

