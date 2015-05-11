__author__ = 'qiong'


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.left = None
        self.right = None

def linkedList_to_BST(head):
    temp = head
    n = 0
    while temp:
        n += 1
        temp = temp.next
    return list_to_BST_helper(head, 0, n)

def list_to_BST_helper(head, s, e):
    curr = None
    if s<e:
        m = s + ((e-s)>>1)
        curr = TreeNode(0)
        curr.left = list_to_BST_helper(head, s, m)
        curr.val = head.val
        head = head.next
        curr.right = list_to_BST_helper(head, m+1, e)
    return curr
'''
node = TreeNode(0)
node.next = TreeNode(1)
node.next.next = TreeNode(2)
print linkedList_to_BST(node)
'''