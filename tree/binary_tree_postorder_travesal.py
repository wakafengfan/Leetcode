"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3


return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?

"""
from .tree_node import TreeNode, root


def binary_tree_postorder_traversal(root: TreeNode):
    result = []
    stack = [(1, root)]
    while stack:
        go_deeper, node = stack.pop()
        if not node:
            continue
        if go_deeper:
            stack.append((0, node))
            stack.append((1, node.right))
            stack.append((1, node.left))
            continue

        result.append(node.val)

    return result

print(binary_tree_postorder_traversal(root=root))