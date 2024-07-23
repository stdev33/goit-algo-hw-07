from trees import BinarySearchTree
from trees import AVLTree


def main():
    values = [21, 7, 23, 6, 15, 12, 14]

    binary_search_tree = BinarySearchTree()
    avl_tree = AVLTree()

    for value in values:
        binary_search_tree.insert(value)
        avl_tree.insert(value)

    print(f"Сума всіх значень у BST: {binary_search_tree.sum_values()}")
    print(f"Сума всіх значень у AVL-дереві: {avl_tree.sum_values()}")


if __name__ == "__main__":
    main()
