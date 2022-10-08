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

    def __str__(self):
        return f"{self.value}" 

             
bst = BST()
bst.insert(7)
bst.insert(6)
bst.insert(8)
bst.insert(2)
bst.insert(5)
bst.insert(2)
bst.insert(10)
print(bst.levelorder())
print(bst.inorder())
print(bst.contains(1)) 
print(bst.postorder())
print(bst.preorder())
print(bst.get_root_data())
print(bst.get_number_of_nodes())
print(bst.get_height())
bst.clear()
