__author__ = 'qiong'

# epi question 6.11
# start time 11:45pm
# end time 12:30pm
# space complexity

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_LCA(root, n1, n2):
    if not root: return None

    if (root==n1 and is_child(root, n2)) or (root==n2 and is_child(root, n1)) or (root==n1 and root==n2):
        return root
    l1 = is_child(root.left, n1)
    l2 = is_child(root.left, n2)
    r1 = is_child(root.right, n1)
    r2 = is_child(root.right, n2)
    if (l1 and r2) or (l2 and r1): return True
    elif (l1 and l2): return find_LCA(root.left, n1, n2)
    elif (r1 and r2): return find_LCA(root.right, n1, n2)
    else: return None

def is_child(root, node):
    if not root: return False
    if root==node: return True
    return is_child(root.left, node) or is_child(root.right)

