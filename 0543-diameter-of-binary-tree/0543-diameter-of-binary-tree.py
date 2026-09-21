class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def solve(root):
            nonlocal diameter

            if root is None:
                return 0

            left = solve(root.left)
            right = solve(root.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        solve(root)
        return diameter