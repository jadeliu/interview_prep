__author__ = 'qiong'

# epi 6.12
# start time 12:46pm
# finish time 12:57 pm


class TreeNode:
    def __init__(self, val):
        self.val= val
        self.left = None
        self.right = None
        self.parent = None

def find_LCA_with_parent(root, n1, n2):
    if (not root) or (not n1) or (not n2): return None
    if root==n1==n2: return root
    l=n1
    while l:
        if is_child(l, n2):
            return l
        l = l.parent
    return None

def is_child(root, node):
    if not root: return False
    if root==node: return True
    return is_child(root.left, node) or is_child(root.right)
