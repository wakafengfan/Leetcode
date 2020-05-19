"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

遍历每一层

"""
from .tree_node import TreeNode, root


def binary_tree_level_order_traversal(root: TreeNode):
    res = []
    current = [root]

    while current:
        next_level, cur_level = [], []  # next_level收集下一层所有节点，val收集当层节点的值
        for node in current:
            cur_level.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        current = next_level  # 指针下移
        res.append(cur_level)
    return res


print(binary_tree_level_order_traversal(root=root))
























