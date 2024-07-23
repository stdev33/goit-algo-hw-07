from trees import BinarySearchTree
from trees import AVLTree


def main():
    values = [21, 7, 23, 6, 15, 12, 14]

    binary_search_tree = BinarySearchTree()
    avl_tree = AVLTree()

    for value in values:
        binary_search_tree.insert(value)
        avl_tree.insert(value)

    print(f"Максимальне значення у BST: {binary_search_tree.find_max()}")
    print(f"Максимальне значення у AVL-дереві: {avl_tree.find_max()}")


if __name__ == "__main__":
    main()
