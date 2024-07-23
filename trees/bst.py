class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.value:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def find_max(self):
        if self.root is None:
            return None
        else:
            return self._find_max(self.root)

    def _find_max(self, root):
        current = root
        while current.right is not None:
            current = current.right
        return current.value

    def find_min(self):
        if self.root is None:
            return None
        else:
            return self._find_min(self.root)

    def _find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.value

    def sum_values(self):
        return self._sum_values(self.root)

    def _sum_values(self, root):
        if root is None:
            return 0
        return root.value + self._sum_values(root.left) + self._sum_values(root.right)
