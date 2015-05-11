__author__ = 'qiong'

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_k_largest_BST(root, k):
    k_elements = []
    find_k_largest_BST_helper(root, k, k_elements)
    return k_elements

def find_k_largest_BST_helper(root, k, k_elements):
    if (root and len(k_elements)<k):
        find_k_largest_BST_helper(root.right, k, k_elements)
        if len(k_elements)<k:
            k_elements.append(root.val)
            find_k_largest_BST_helper(root.left, k, k_elements)

root = TreeNode(1)
root.left = TreeNode(0)
root.right =TreeNode(2)
a = root.left
a.left = TreeNode(-2)

print find_k_largest_BST(root, 3)