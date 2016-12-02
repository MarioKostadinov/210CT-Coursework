#  Implement the TREE_SORT algorithm in a language of your choice,
#  based on the template provided on Moodle, but make sure that
#  the INORDER function is implemented iteratively, rather than recursively.


Task 12


# include <iostream>

class BinTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_insert(tree, item):
    if tree == None:
        tree = BinTreeNode(item)
    else:
        if (item < tree.value):
            if (tree.left == None):
                tree.left = BinTreeNode(item)
            else:
                tree_insert(tree.left, item)
        else:
            if (tree.right == None):
                tree.right = BinTreeNode(item)
            else:
                tree_insert(tree.right, item)
    return tree


def postorder(tree):
    if (tree.left != None):
        postorder(tree.left)
    if (tree.right != None):
        postorder(tree.right)
    print
    tree.value


def in_order(tree):
    if (tree.left != None):
        in_order(tree.left)
    print
    tree.value
    if (tree.right != None):
        in_order(tree.right)


def in_order_iterеtaion(tree, size):
    size_of_tree = size * 3
    a_list = []
    for i in range(size_of_tree):
        try:
            if tree!=None:
                a_list.append(tree)
                tree=tree.left
            else:
                try:
                    tree = a_list.pop()
                except IndexError:
                    pass
                print(tree.value)
                tree = tree.right
        except AttributeError:
            pass


if __name__ == '__main__':
    t = tree_insert(None, 6);
    tree_insert(t, 10)
    tree_insert(t, 5)
    tree_insert(t, 2)
    tree_insert(t, 3)
    tree_insert(t, 4)
    tree_insert(t, 11)
    in_order(t)

