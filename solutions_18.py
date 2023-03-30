# Definition for a binary tree node.
# A binary tree is a data structure in which each node has at most two child nodes,
# which are referred to as the left child and the right child. The topmost node in
# a binary tree is called the root. The left and right subtrees of a node in a binary
# tree are also binary trees. The leaf nodes, which have no children, are the terminal
# nodes of a binary tree. Binary trees are often used for searching and sorting data.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        result = []
        if root is None:
            return result
        result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        result.extend(self.inorderTraversal(root.right))
        return result

# Create the TreeNode object
root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
calculus = TreeNode(1,2,3)
# Call inorderTraversal to get the inorder traversal of the tree
result = Solution().inorderTraversal(root)

# Check if the result is correct
assert result == [1, 3, 2]