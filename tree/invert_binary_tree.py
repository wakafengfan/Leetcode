"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

"""
from tree.tree_node import TreeNode


def invert_binary_tree(root: TreeNode):
    if not root:
        return None
    stack = [root]   # stack存放还没有做对换的节点
    while stack:
        node = stack.pop()
        if not node:
            continue
        node.left, node.right = node.right, node.left
        stack.append(node.left)
        stack.append(node.right)
    return root


t = TreeNode(4)
t.left = TreeNode(2)
t.left.left = TreeNode(1)
t.left.right = TreeNode(3)

t.right = TreeNode(7)
t.right.left = TreeNode(6)
t.right.right = TreeNode(9)

print(invert_binary_tree(t))


