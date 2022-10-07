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

        if self.value >= value:
            if self.left:
                self.left.insert(value)

            else:
                self.left = BST(value)

            return    

        if self.value < value:
            if self.right:
                self.right.insert(value)

            else:
                self.right = BST(value)
            return
   

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

    def get_number_of_nodes(self):
        return self.counter

    def get_root_data(self):
        return self.value    


    def __str__(self):
        return f"{self.value}"   

bst = BST()

bst.insert(7)
bst.insert(7)
bst.insert(8)
bst.insert(2)
bst.insert(5)
bst.insert(2)
           
print(bst.get_number_of_nodes())
print(bst.get_root_data())
print(bst.postorder())
print(bst.preorder())








