class BST:
    counter = 0
    def __init__(self, value=None):
        self.right = None
        self.left = None
        self.value = value
        BST.counter += 1

    def __del__(self):
        BST.counter -= 1

    def insert(self, value):
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
       self.right = None
       self.left = None
       self.value = None        

    def contains(self, value):
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
        return self.contains(value)
           
    def inorder(self, values=[]):
        if self.left:
            self.left.inorder(values)

        if self.value:
            values.append(self.value)

        if self.right:
            self.right.inorder(values)
        return values            
             
    def postorder(self, values=[]):
        if self.left:
            self.left.postorder(values)

        if self.right:
            self.right.postorder(values)

        if self.value:
            values.append(self.value)

        return values

    def preorder(self, values=[]):
        if self.value:
            values.append(self.value)

        if self.left:
            self.left.preorder(values)

        if self.right:
            self.right.preorder(values)

        return values

    def __printCurrentLevel(self, level):
        if self is None:
            return

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
        h = self.get_height()
        for i in range(1, h + 1):
            self.__printCurrentLevel(i)

        return ""

    def get_number_of_nodes(self):
        return self.counter

    def get_root_data(self):
        return self.value

    def get_height(self):
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
        return not self.__eq__(other)

    def __add__(self, other):
        if not self and not other:
            return None
        value1 = self.value if self else 0
        value2 = other.value if other else 0

        root = BST(value1 + value2)

        root.left = BST.__add__(self.left if self else None, other.left if other else None)
        root.right = BST.__add__(self.right if self else None, other.right if other else None)

        return root

    def __iadd__(self, other):
        if not self and not other:
            return None
        value1 = self.value if self else 0
        value2 = other.value if other else 0

        root = BST(value1 + value2)

        root.left = BST.__iadd__(self.left if self else None, other.left if other else None)
        root.right = BST.__iadd__(self.right if self else None, other.right if other else None)

        self = root

        return self

    def __str__(self):
        return self.levelorder()

             
bst = BST()
bst.insert(7)
bst.insert(6)
bst.insert(2)
bst.insert(5)
bst.insert(8)
#bst.erase(2)
bst1 = BST()
bst1.insert(7)
bst1.insert(6)
bst1.insert(1)
bst1.insert(2)
bst1.insert(5)
print(bst.find(8))
print(bst == bst1)
print(bst.postorder())
print(bst + bst1)


