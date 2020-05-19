"""

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?





solution: https://zxi.mytechroad.com/blog/tree/leetcode-99-recover-binary-search-tree/


"""
from tree.tree_node import TreeNode


class RecoverTree(object):
    def __init__(self):
        self.first, self.second, self.pre = None, None, None

    def in_order(self, root: TreeNode):
        if not root: return
        self.in_order(root.left)

        if self.pre and self.pre.val > root.val:
            if not self.first: self.first = self.pre
            self.second = root

        self.pre = root

        self.in_order(root.right)

    def recover_tree(self, root: TreeNode):

        self.in_order(root)

        self.first.val, self.second.val = self.second.val, self.first.val


r = TreeNode(3)
r.left = TreeNode(1)
r.right = TreeNode(4)
r.right.left = TreeNode(2)

recover = RecoverTree()
recover.recover_tree(r)






