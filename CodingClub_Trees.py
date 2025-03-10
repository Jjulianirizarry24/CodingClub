from collections import deque
from collections import defaultdict

# ------------------------------- Class Definition -------------------------------

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# ------------------------------- Tree Traversal -------------------------------
def preorder(root):
    if root:
        print(root.value, end=" ")  # Visit the root node
        preorder(root.left)  # Traverse the left subtree
        preorder(root.right)  # Traverse the right subtree

def inorder(root):
    if root:
        inorder(root.left)  # Traverse the left subtree
        print(root.value, end=" ")  # Visit the root node
        inorder(root.right)  # Traverse the right subtree

def postorder(root):
    if root:
        postorder(root.left)  # Traverse the left subtree
        postorder(root.right)  # Traverse the right subtree
        print(root.value, end=" ")  # Visit the root node

def dfs(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.value, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def bfs(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)



# ------------------------------- Excercises -------------------------------

#1
def search_bst(root, target):
    if not root:
        return False
    if root.val == target: 
        return True
    elif target < root.val:
        return search_bst(root.left, target)
    else:
        return search_bst(root.right, target)

#2 TODO: Add tests
def invertTree(root):
    if not root:
        return root
    root.left, root.right = root.right,root.left
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root

#3 TODO: Add tests
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    dct = defaultdict(list)
    if not root:
        return []
    def traversal(node,level):
        if not node:
            return
        dct[level].append(node.val)
        traversal(node.left,level+1)
        traversal(node.right,level+1)
    traversal(root,0)
    return list(dct.values())


# ------------------------------- Solutions -------------------------------

# # Traversal examples:
# if __name__ == "__main__":
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(3)
#     root.left.left = TreeNode(4)
#     root.left.right = TreeNode(5)
#     root.right.left = TreeNode(6)
#     root.right.right = TreeNode(7)
    
#     print("Pre-order Traversal:")
#     preorder(root)
#     print("\nIn-order Traversal:")
#     inorder(root)
#     print("\nPost-order Traversal:")
#     postorder(root)
#     print("\nIterative DFS Traversal:")
#     iterative_dfs(root)
#     print("\nBFS Traversal:")
#     bfs(root)



# # => Excercise #1
# root = TreeNode(8)
# root.left = TreeNode(3)
# root.right = TreeNode(10)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(6)
# root.left.right.left = TreeNode(4)
# root.left.right.right = TreeNode(7)
# root.right.right = TreeNode(14)
# root.right.right.left = TreeNode(13)

# print(search_bst(root, 6))  # True
# print(search_bst(root, 2))  # False

