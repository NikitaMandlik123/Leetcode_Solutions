# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        q1 = [root]
        sol = []
        
        while q1:
            levelSum = 0
            levelNodes = len(q1)
            len_q = levelNodes
            
            while len_q :
                node = q1.pop(0)
                levelSum+= node.val
                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)
                len_q -=1
            sol.append(levelSum/levelNodes)
        return sol