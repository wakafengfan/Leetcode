"""

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


"""
from tree.tree_node import TreeNode


def generate_bst_main(n):

    def generate_bst(start, end):
        res = []
        if start > end: res.append(None)

        for i in range(start, end+1):
            left = generate_bst(start, i-1)
            right = generate_bst(i+1, end)

            for j in left:
                for k in right:
                    cur = TreeNode(i)
                    cur.left = j
                    cur.right = k
                    res.append(cur)

        return res
    a = generate_bst(1, n)
    return a


print(generate_bst_main(3))
