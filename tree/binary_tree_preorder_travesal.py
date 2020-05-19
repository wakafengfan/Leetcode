"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?

前序遍历：中左右

"""
from .tree_node import TreeNode, root


def binary_tree_preorder_traversal(root: TreeNode):
    result = []
    stack = [(1, root)]
    while stack:
        go_deeper, node = stack.pop()
        if not node:
            continue
        if go_deeper:  # 栈 右左中；遍历：中左右。
            stack.append((1, node.right))
            stack.append((1, node.left))
            stack.append((0, node))
        else:
            result.append(node.val)
    return result

print(binary_tree_preorder_traversal(root=root))