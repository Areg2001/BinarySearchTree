class BST:

    def __init__(self, value=None):
        self.right = None
        self.left = None
        self.value = value
        
    def insert(self, value):
        """This function takes one argument and is inserting it into the BST."""

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
        """This function takes one argument and deleting it if BST contain it, otherwise it does not do anything."""
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

        if self.right == None:
            return self.left

        if self.left == None:
            return self.right

        min_bigger_node = self.right

        while min_bigger_node.left:
            min_bigger_node = min_bigger_node.left

        self.value = min_bigger_node.value
        self.right = self.right.erase(min_bigger_node.value)

        return self

    def clear(self):
        """This function is deleting BST."""

        self.right = None
        self.left = None
        self.value = None


    def contains(self, value):
        """This function takes one argument and find it into BST. If BST contain, function returns True else False."""

        if not self.value:
            return False

        if self.value == value:
            return True

        if value <= self.value:
            if not self.left:
                return False

            return self.left.contains(value)

        else:
            if not self.right:
                return False

            return self.right.contains(value)

    def find(self, value):
        """This function takes one argument and find it into BST. If BST contain, function returns True else False."""

        return self.contains(value)

    def inorder(self, values=[]):
        """This function returns list of BST's values in order."""
        if self.left:
            self.left.inorder(values)

        if self.value:
            values.append(self.value)

        if self.right:
            self.right.inorder(values)
        return values

    def postorder(self):
        """This function returns list of BST's values in post order."""
        if self.left:
            self.left.postorder()

        if self.right:
            self.right.postorder()

        if self.value:
            print(self.value, end=" ")

        return " "

    def preorder(self, values=[]):
        """This function returns list of BST's values in pre order."""

        if self.value:
            values.append(self.value)

        if self.left:
            self.left.preorder(values)

        if self.right:
            self.right.preorder(values)

        return values

    def __printCurrentLevel(self, level):

        if self is None:
            return self

        if level == 1:
            print(self.value, end=" ")

        elif self.value > 1:
            if self.left and self.right:
                self.left.__printCurrentLevel(level - 1)
                self.right.__printCurrentLevel(level - 1)

            elif self.left:
                self.left.__printCurrentLevel(level - 1)

            elif self.right:
                self.right.__printCurrentLevel(level - 1)

    def levelorder(self):
        """This function returns BST's values in level order."""

        h = self.get_height()
        for i in range(1, h + 1):
            self.__printCurrentLevel(i)

        return " "

    def merge(self, other):
        """This function returns list of two merged BST's values."""
        pass

    def get_number_of_nodes(self):
        """This function returns count of BST nodes."""
        
        if self.left and self.right:
            return 1 + self.left.get_number_of_nodes() + self.right.get_number_of_nodes()

        elif self.left:
            return 1 + self.left.get_number_of_nodes()

        elif self.right:
            return 1 + self.right.get_number_of_nodes()

        else:
            return 1

    
    def get_root_data(self):
        """This function returns BST root value."""

        return self.value

    def get_height(self):
        """This function returns BST's height."""

        if self.value is None:
            return 0

        if self.left and self.right:
            return 1 + max(self.left.get_height(), self.right.get_height())

        elif self.left:
            return 1 + self.left.get_height()

        elif self.right:
            return 1 + self.right.get_height()

        else:
            return 1

    def __eq__(self, other):
        """This method checks if two BST are equal or not, and returns True if equal else False."""

        if (not self) and (not other):
            return True

        if (self and other) and self.value == other.value:
            left = self.left.__eq__(other.left)
            right = self.right.__eq__(other.right)

            if left and right:
                return True

            return False

        return False

    def __ne__(self, other):
        """This method checks if two BST are equal or not, and returns True if not equal else False."""

        return not self.__eq__(other)

    def __add__(self, other):
        """This method is adding two BST."""

        if not self and not other:
            return None
        value1 = self.value if self else 0
        value2 = other.value if other else 0

        root = BST(value1 + value2)

        root.left = BST.__add__(self.left if self else None, other.left if other else None)
        root.right = BST.__add__(self.right if self else None, other.right if other else None)

        return root

    def __iadd__(self, other):
        """This method is adding two BST and assign it BST, which was writed first."""
        if not self and not other:
            return None
        value1 = self.value if self else 0
        value2 = other.value if other else 0

        root = BST(value1 + value2)

        root.left = BST.__iadd__(self.left if self else None, other.left if other else None)
        root.right = BST.__iadd__(self.right if self else None, other.right if other else None)

        self = root

        return self

    def __str__(self, other=None):
        return f"{self.postorder()}"



bst = BST()
bst.insert(7)
bst.insert(6)
bst.insert(2)
bst.insert(5)
bst.insert(8)
bst1 = BST()
bst1.insert(7)
bst1.insert(6)
bst.erase(2)
bst1.insert(6)
bst1.insert(8)
bst1.insert(5)
print(bst.levelorder())
print(bst.preorder())
print(bst.postorder())
print(bst.inorder())
print(bst1)
print(bst)
print(bst.merge(bst1))
print(bst.get_root_data())
print(bst.contains(7))
print(bst1.contains(3))
print(bst.find(5))
print(bst1.find(7))
print(bst.get_number_of_nodes())
print(bst1.get_number_of_nodes())
print((bst + bst1).get_number_of_nodes())
print(bst == bst1)
print(bst != bst1)
bst += bst1
print(bst)