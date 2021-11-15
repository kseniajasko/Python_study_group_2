class TreeNode:

    def __init__(self, data=None):
        self.left = None
        self.data = data
        self.right = None

    def __repr__(self):
        return f'{self.data}'

    def add(self, data):
        if data < self.data:
            if self.left:
                self.left.add(data)
            else:
                self.left = TreeNode(data)
        elif data > self.data:
            if self.right:
                self.right.add(data)
            else:
                self.right = TreeNode(data)


class BinaryTree:

    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self.root.add(data)

    def contains(self, data):
        node = self.root
        while node:
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
            else:
                return True
        return False

    def find(self, data):
        node = self.root
        while node:
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
            else:
                return node
        return None

    def find_closest(self, data):
        node = self.root
        closest_node = node
        closest_min_diff = abs(data - node.data)
        while node:
            if abs(data - node.data) == closest_min_diff:
                raise ValueError('Equidistant elements')
            elif abs(data - node.data) < closest_min_diff:
                closest_min_diff = abs(data - node.data)
                closest_node = node

            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
            else:
                return node
        return closest_node

    def delete_tree(self):
        self.root = None

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(str(node.data) + ' ')
            self._print_tree(node.right)

tree = BinaryTree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.add(10)
tree.add(14)
print(tree.find_closest(10))
#tree.delete_tree()
tree.print_tree()





