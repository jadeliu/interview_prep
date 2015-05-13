__author__ = 'qiong'

# start time 9:44pm
# end time 10:45pm
# time complexity O(n)
# space complexity O(1)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def inorder_traversal(root):
    if not root:
        return None
    prev = None
    curr = root
    next = None
    while curr:
        if prev==curr.left:
            print curr.val
            if curr.right:
                next = curr.right
            else:
                next = curr.parent
        elif prev==curr.right:
            next==curr.parent
        else:
            if curr.left:
                next = curr.left
            else:
                print curr.val
                if curr.right:
                    next = curr.right
                else:
                    next = curr.parent
        prev = curr
        curr = next

a = TreeNode(3)
b = TreeNode(4)
c = TreeNode(5)
d = TreeNode(6)
a.left = b
b.left = c
a.right = d
b.parent = a
d.parent = a
c.parent = b
print inorder_traversal(a)
