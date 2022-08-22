class Tree:
    def __init__(self,val = None):
        if val != None:
            self.val = val
        else:
            self.val=None
        self.left=None
        self.right=None

    def insert(self,val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Tree(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                 self.right = Tree(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

    def values(self):
        if self.left:
            self.left.values()

        print(self.val)

        if self.right:
            self.right.values()


tree = Tree(19)
tree.left = Tree(20)
tree.right=Tree(23)
tree.insert(57)
tree.insert(67)
tree.insert(99)

tree.values()
