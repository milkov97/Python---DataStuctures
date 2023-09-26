class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)  # calling the recursive method for insert
        # new_node = Node(value)
        # if self.root is None:
        #     self.root = new_node
        #     return True
        # temp = self.root
        # while temp:
        #     if new_node.value == temp.value:
        #         return False
        #     if new_node.value < temp.value:
        #         if temp.left is None:
        #             temp.left = new_node
        #             return True
        #         temp = temp.left
        #     else:
        #         if temp.right is None:
        #             temp.right = new_node
        #         temp = temp.right

    def contains(self, value):
        return self.__r_contains(self.root, value)  # calling the recursive method for contains
        # temp = self.root
        # while temp:
        #     if value < temp.value:
        #         temp = temp.left
        #     elif value > temp.value:
        #         temp = temp.right
        #     else:
        #         return True
        # return False

    def delete_node(self, value):
        self.__delete_node(self.root, value)

    def __r_contains(self, current_node, value):
        """Recursive method to check for given value"""
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def __r_insert(self, current_node, value):
        """Recursive method for insert a value in tree"""
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def __delete_node(self, current_node, value):
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node

    @staticmethod
    def min_value(current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def bfs(self):
        curr_node = self.root
        queue = []
        result = []
        queue.append(curr_node)

        while len(queue) > 0:
            curr_node = queue.pop(0)
            result.append(curr_node.value)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        return result

    def dfs_pre_order(self):
        result = []

        def traverse(current_node):
            result.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return result

    def dfs_post_order(self):
        result = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            result.append(current_node.value)
        traverse(self.root)
        return result

    def dfs_in_order(self):
        result = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            result.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)
        traverse(self.root)
        return result


tree = BinarySearchTree()
tree.insert(47)
tree.insert(21)
tree.insert(76)
tree.insert(18)
tree.insert(27)
tree.insert(52)
tree.insert(82)

print(tree.contains(21))
print(tree.contains(18))
print(tree.contains(17))
print(tree.bfs())
print(tree.dfs_pre_order())
print(tree.dfs_post_order())
print(tree.dfs_in_order())