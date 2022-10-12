"""Main Module"""


class BST:
    """Binary Search Tree"""

    def __init__(self, value=None):
        self.right = None
        self.left = None
        self.value = value

    def insert(self, value):
        """This method takes a value and inserts the value in the BST."""

        if not self.value:
            self.value = value
            return

        if self.value >= value:
            if self.left:
                self.left.insert(value)

            else:
                self.left = BST(value)

        if self.value < value:
            if self.right:
                self.right.insert(value)

            else:
                self.right = BST(value)

    def erase(self, value):
        """This method takes a value and deletes the value from BST
           If there is no any node with the given value, doesn't do anything.
        """
        if self is None:
            return None

        if value < self.value:
            if self.left:
                self.left = self.left.erase(value)

            return self

        if value > self.value:
            if self.right:
                self.right = self.right.erase(value)

            return self

        if not self.right:
            return self.left

        if not self.left:
            return self.right

        min_bigger_node = self.right

        while min_bigger_node.left:
            min_bigger_node = min_bigger_node.left

        self.value = min_bigger_node.value
        self.right = self.right.erase(min_bigger_node.value)

        return self

    def clear(self):
        """This method deletes all nodes from BST."""

        self.right = None
        self.left = None
        self.value = None

    def contains(self, value):
        """This method takes a value and checks whether the value is in BST."""

        if not self.value:
            return False

        if self.value == value:
            return True

        if value <= self.value:
            if not self.left:
                return False

            return self.left.contains(value)

        if not self.right:
            return False

        return self.right.contains(value)

    def find(self, value):
        """This method takes a value and checks whether the value is in BST."""

        return self.contains(value)

    def inorder(self, values=None):
        """This method returns list of BSTs values in order."""
        if values is None:
            values = []

        if self.left:
            self.left.inorder(values)

        if self.value:
            values.append(self.value)

        if self.right:
            self.right.inorder(values)
        return values

    def postorder(self):
        """This method returns list of BSTs values in post-order."""
        if self.left:
            self.left.postorder()

        if self.right:
            self.right.postorder()

        if self.value:
            print(self.value, end=" ")

        return " "

    def preorder(self, values=None):
        """This method returns list of BSTs values in pre-order."""

        if values is None:
            values = []

        if self.value:
            values.append(self.value)

        if self.left:
            self.left.preorder(values)

        if self.right:
            self.right.preorder(values)

        return values

    def __print_current_level(self, level):

        if self is None:
            return self

        if level == 1:
            print(self.value, end=" ")

        elif self.value > 1:
            if self.left and self.right:
                self.left.__print_current_level(level - 1)
                self.right.__print_current_level(level - 1)

            elif self.left:
                self.left.__print_current_level(level - 1)

            elif self.right:
                self.right.__print_current_level(level - 1)

    def level_order(self):
        """This method returns BSTs values in level-order."""

        height = self.get_height()

        for i in range(1, height + 1):
            self.__print_current_level(i)

        return " "

    def merge(self, other):
        """This method returns list of two merged BSTs values."""

        arr = self.inorder() + other.inorder()

        swapped = True

        while swapped:
            swapped = False
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
        return arr

    def get_number_of_nodes(self):
        """This method returns the count of BST nodes."""

        if self.left and self.right:
            return 1 + self.left.get_number_of_nodes() + self.right.get_number_of_nodes()

        if self.left:
            return 1 + self.left.get_number_of_nodes()

        if self.right:
            return 1 + self.right.get_number_of_nodes()

        return 1

    def get_root_data(self):
        """This method returns BSTs root value."""

        return self.value

    def get_height(self):
        """This method returns BSTs height."""

        if self.value is None:
            return 0

        if self.left and self.right:
            return 1 + max(self.left.get_height(), self.right.get_height())

        if self.left:
            return 1 + self.left.get_height()

        if self.right:
            return 1 + self.right.get_height()

        return 1

    def __eq__(self, other):
        """This method checks whether two BSTs are equal."""

        if (not self) and (not other):
            return True

        if (self and other) and self.value == other.value:
            left = self.left.__eq__(other.left)
            right = self.right.__eq__(other.right)

            if left and right:
                return True

        return False

    def __ne__(self, other):
        """This method checks whether two BSTs are not equal."""

        return not self.__eq__(other)

    def __add__(self, other):
        """This method adds two BSTs."""

        if not self and not other:
            return None

        value1 = self.value if self else 0
        value2 = other.value if other else 0

        root = BST(value1 + value2)

        root.left = BST.__add__(self.left if self else None, other.left if other else None)
        root.right = BST.__add__(self.right if self else None, other.right if other else None)

        return root

    def __iadd__(self, other):
        """This method adds two BSTs and assign the result to the instance."""

        if not self and not other:
            return None

        value1 = self.value if self else 0
        value2 = other.value if other else 0

        root = BST(value1 + value2)

        root.left = BST.__iadd__(self.left if self else None, other.left if other else None)
        root.right = BST.__iadd__(self.right if self else None, other.right if other else None)

        return root

    def __str__(self):
        return f"{self.inorder()}"
