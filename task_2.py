from trees import BinarySearchTree
from trees import AVLTree


def main():
    values = [21, 7, 23, 6, 15, 12, 14]

    binary_search_tree = BinarySearchTree()
    avl_tree = AVLTree()

    for value in values:
        binary_search_tree.insert(value)
        avl_tree.insert(value)

    print(f"Найменше значення у BST: {binary_search_tree.find_min()}")
    print(f"Найменше значення у AVL-дереві: {avl_tree.find_min()}")


if __name__ == "__main__":
    main()
