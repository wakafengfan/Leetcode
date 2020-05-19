"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

递归的方式相对简单，非递归的方式借助栈这种数据结构实现起来会相对轻松。

如果采用非递归，可以用栈(Stack)的思路来处理问题。

中序遍历的顺序为左-根-右，具体算法为：

从根节点开始，先将根节点压入栈

然后再将其所有左子结点压入栈，取出栈顶节点，保存节点值

再将当前指针移到其右子节点上，若存在右子节点，则在下次循环时又可将其所有左子结点压入栈中， 重复上步骤

"""
from .tree_node import TreeNode, root


def binary_tree_inorder_traversal(root: TreeNode):
    result = []
    stack = [(1, root)]
    while stack:
        go_deeper, node = stack.pop()
        if not node:
            continue
        if go_deeper:
            stack.append((1, node.right))
            stack.append((0, node))
            stack.append((1, node.left))
            continue
        result.append(node.val)

    return result

print(binary_tree_inorder_traversal(root=root))
