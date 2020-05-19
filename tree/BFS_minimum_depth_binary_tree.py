"""


Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

"""
from tree.tree_node import TreeNode


def min_depth(root: TreeNode):
    if not root: return 0
    q = [root]
    step = 1
    while q:
        n = len(q)
        for _ in range(n):
            node = q.pop(0)
            if not node:
                continue
            if not node.left and not node.right:
                return step
            q.append(node.left)
            q.append(node.right)
        step += 1
    return step


def max_depth(root: TreeNode):
    if not root: return 0
    q = [root]
    step = 1
    all_step = []
    while q:
        n = len(q)
        for _ in range(n):
            node = q.pop(0)
            if not node:
                continue
            if not node.left and not node.right:
                all_step.append(step)

            q.append(node.left)
            q.append(node.right)
        step += 1
    return max(all_step)


t = TreeNode(3)
t.left = TreeNode(9)

t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)

print(min_depth(t))
print(max_depth(t))