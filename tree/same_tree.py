"""

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

"""
from tree.tree_node import TreeNode


def same(root1: TreeNode, root2: TreeNode):
    if not root1 and not root2: return True
    if not root1 or not root2: return False
    if root1.val != root2.val: return False

    return same(root1.left, root2.left) and same(root1.right, root2.right)


