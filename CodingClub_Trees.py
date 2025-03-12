from collections import deque
from collections import defaultdict
import unittest

# ------------------------------- Tree Visualization -------------------------------
def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.value))
        if root.left or root.right:
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")

# ------------------------------- Class Definition -------------------------------
class TreeNode:
    def __init__(self, value):
        self.val = value
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
    
def invertTree(root):
    if not root:
        return root
    root.left, root.right = root.right,root.left
    invertTree(root.left)
    invertTree(root.right)
    return root

def levelOrder(self, root):
    dct = defaultdict(list)
    queue = deque()
    
    queue.append((root,0))

    while(queue):
        temp, level = queue.pop()
        if not temp:
            continue
        l,r = temp.left, temp.right
        dct[level].append(temp.val)
        if temp.left:
            queue.appendleft((temp.left,level+1))
        if temp.right:
            queue.appendleft((temp.right,level+1))
                
    return list(dct.values())


# ------------------------------- Solutions -------------------------------

class TestBinaryTreeFunctions(unittest.TestCase):
    def setUp(self):
        # Creating the following BST:
        #        4
        #       / \
        #      2   7
        #     / \  / \
        #    1  3 6  9
        self.root = TreeNode(4)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(7)
        self.root.left.left = TreeNode(1)
        self.root.left.right = TreeNode(3)
        self.root.right.left = TreeNode(6)
        self.root.right.right = TreeNode(9)

    # Test cases for search_bst
    def test_search_bst_found(self):
        self.assertTrue(search_bst(self.root, 6))  # Value 6 exists

    def test_search_bst_not_found(self):
        self.assertFalse(search_bst(self.root, 10))  # Value 10 does not exist

    # Test cases for invertTree
    def test_invert_tree(self):
        inverted_root = invertTree(self.root)
        self.assertEqual(inverted_root.left.val, 7)  # Root's left should now be 7
        self.assertEqual(inverted_root.right.val, 2)  # Root's right should now be 2

    def test_invert_tree_single_node(self):
        single_node = TreeNode(5)
        inverted_single = invertTree(single_node)
        self.assertEqual(inverted_single.val, 5)
        self.assertIsNone(inverted_single.left)
        self.assertIsNone(inverted_single.right)

    # Test cases for levelOrder
    def test_level_order(self):
        result = levelOrder(self, self.root)
        self.assertEqual(result, [[4], [2, 7], [1, 3, 6, 9]])

    def test_level_order_empty_tree(self):
        self.assertEqual(levelOrder(self,None), [])  # Empty tree should return an empty list

if __name__ == '__main__':
    unittest.main()
