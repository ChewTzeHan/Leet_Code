# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return
        #print(root.val)
        return Traverse(root, [])

def Traverse(node, path):
    if node.left:
        Traverse(node.left, path)
    
    path.append(node.val)
    if node.right:
        Traverse(node.right, path)
    


    return path