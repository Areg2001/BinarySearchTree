class BST:
    counter = 0
    def __init__(self, value=None):
        self.right = None
        self.left = None
        self.value = value
        BST.counter += 1

    def insert(self, value):
        if not self.value:
            self.value = value
            return

        if self.value == value:
            return 

        if self.value > value:
            if self.left:
                self.left.insert(value)
                return

            self.left = BST(value)
            return

        if self.value < value:
            if self.right:
                self.right.insert(value)
                return

            self.right = BST(value)
            return
   

    def postorder(self, values=[]):

        if self.left != None:
            self.left.postorder(values)

        if self.right != None:
            self.right.postorder(values)

        if self.value != None:
            values.append(self.value)

        return values

    def preorder(self, values=[]):
        if self.value != None:
            values.append(self.value)

        if self.left != None:
            self.left.preorder(values)

        if self.right != None:
            self.right.preorder(values)

        return values                                     

    def get_number_of_nodes(self):
        return self.counter

    def get_root_data(self):
        return self.value    


    def __str__(self):
        return f"{self.value}"   

bst = BST()

l1 = [6, 5, 7, 12, 8, 4, 3, 2, 13]

for num in l1:
    bst.insert(num)
           
print(bst.get_number_of_nodes())
print(bst.get_root_data())
print(bst.postorder())
print(bst.preorder())








