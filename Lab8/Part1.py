class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            root = Node(data)
            return root
        else:
            if data < root.data:
                root.left = self.insert(root.left, data)
                root.left.parent = root
            else:
                root.right = self.insert(root.right, data)
                root.right.parent = root
        return root

    def search(self, root, data):
        if root is None or root.data == data:
            return root
        elif data < root.data:
            return self.search(root.left, data)
        else:
            return self.search(root.right, data)

    def delete(self, root, data):
        if root is None:
            return root
        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.minValueNode(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        return root

    def inOrderTraversal(self, root):
        if root:
            self.inOrderTraversal(root.left)
            print(root.data)
            self.inOrderTraversal(root.right)

    def preOrderTraversal(self, root):
        if root:
            print(root.data)
            self.preOrderTraversal(root.left)
            self.preOrderTraversal(root.right)

    def postOrderTraversal(self, root):
        if root:
            self.postOrderTraversal(root.left)
            self.postOrderTraversal(root.right)
            print(root.data)

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def VisualizeTree(self, root, space):
        if root is None:
            return
        space += 10
        self.VisualizeTree(root.right, space)
        print()
        for i in range(10, space):
            print(end=" ")
        print(root.data)
        self.VisualizeTree(root.left, space)


def main():
    bst = BinarySearchTree()
    root = None
    root = bst.insert(root, 50)
    bst.VisualizeTree(root, 0)
    root = bst.insert(root, 60)
    bst.VisualizeTree(root, 0)
    root = bst.insert(root, 20)
    bst.VisualizeTree(root, 0)
    root = bst.insert(root, 40)
    bst.VisualizeTree(root, 0)
    # root = bst.insert(root, 70)
    # root = bst.insert(root, 60)
    # root = bst.insert(root, 80)
    # print("Inorder traversal of the given tree")
    # bst.inOrderTraversal(root)
    # print("\nDelete 20")
    # root = bst.delete(root, 20)
    # print("Inorder traversal of the modified tree")
    # bst.inOrderTraversal(root)
    # print("\nDelete 30")
    # root = bst.delete(root, 30)
    # print("Inorder traversal of the modified tree")
    # bst.inOrderTraversal(root)
    # print("\nDelete 50")
    # root = bst.delete(root, 50)
    # print("Inorder traversal of the modified tree")
    # bst.inOrderTraversal(root)
    # print("\nDelete 70")
    # root = bst.delete(root, 70)
    # print("Inorder traversal of the modified tree")
    # bst.inOrderTraversal(root)
    # print("\nDelete 80")
    # root = bst.delete(root, 80)
    # print("Inorder traversal of the modified tree")
    # bst.inOrderTraversal(root)
    # print("\nDelete 60")
    # root = bst.delete(root, 60)
    # print("Inorder traversal of the modified tree")
    # bst.inOrderTraversal(root)
    # print("\nDelete 40")
    # root = bst.delete(root, 40)
    # print("Inorder traversal of the modified tree")
    # bst.inOrderTraversal(root)
    # print("\nDelete 50")
    # root = bst.delete(root, 50)
    # print("Inorder traversal of the modified tree")
    # bst.inOrderTraversal(root)
    # print("\nDelete 30")
    # root = bst.delete(root, 30)
    # print("Inorder traversal of the modified tree")
    # bst.inOrderTraversal(root)
    # print("\nDelete 20")
    # root = bst.delete(root, 20)
    # print("Inorder traversal of the modified tree")
    # bst.inOrderTraversal(root)
    # print("\nDelete 40")
    # root = bst.delete(root, 40)
    # print("Inorder traversal of the modified tree")
    # bst.inOrderTraversal(root)
    # print("\nDelete 60")


if __name__ == "__main__":
    main()
