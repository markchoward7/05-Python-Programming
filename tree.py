class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self, root):
        self.root = TreeNode(root)

    
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder(self.root, "")


    def preorder(self, start, traversal):
        traversal += str(start.value) + '-'
        if start.left is not None:
            traversal = self.preorder(start.left, traversal)
        if start.right is not None:
            traversal = self.preorder(start.right, traversal)
        return traversal


    def inorder(self, start, traversal):
        if start.left is not None:
            traversal = self.inorder(start.left, traversal)
        traversal += str(start.value) + '-'
        if start.right is not None:
            traversal = self.inorder(start.right, traversal)
        return traversal


    def postorder(self, start, traversal):
        if start.left is not None:
            traversal = self.postorder(start.left, traversal)
        if start.right is not None:
            traversal = self.postorder(start.right, traversal)
        traversal += str(start.value) + '-'
        return traversal

bt = BinaryTree("D")
bt.root.left = TreeNode("B")
bt.root.right = TreeNode("F")
bt.root.left.left = TreeNode("A")
bt.root.left.right = TreeNode("C")
bt.root.right.left = TreeNode("E")
bt.root.right.right = TreeNode("G")

print(bt.print_tree("preorder").strip('-'))
print(bt.print_tree("inorder").strip('-'))
print(bt.print_tree("postorder").strip('-'))