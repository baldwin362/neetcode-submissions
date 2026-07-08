# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Using Breadth First Search Traversal to return level order traversal as nested list
        Arguments:
        root : Optional[TreeNode]
        Return type : List[List[int]]
        >>> root = [1,2,3,4,5,6,7]
        [[1],[2,3],[4,5,6,7]]
        """

        q = deque()
        L = [] #nested list
        if root:
            q.append(root)
            L.append([root.val])
            if not root:
                return []    
        while len(q) > 0: 
            nested_list = []
            for i in range(len(q)):
                root = q.popleft()
                if root.left: 
                    nested_list.append(root.left.val)
                    q.append(root.left)
                if root.right:
                    nested_list.append(root.right.val)
                    q.append(root.right)
            if nested_list:
                L.append(nested_list)
        return L 

            

