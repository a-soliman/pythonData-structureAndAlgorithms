class BST(object):
      def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
      
      def isLeaf(self):
            return self.left == None and self.right == None
      
      def insert(self, value):
            if value <= self.value:
                  if self.left == None:
                        newTree = BST(value)
                        self.left = newTree

                  else:
                        return self.left.insert(value)
            else:
                  if self.right == None:
                        newTree = BST(value)
                        self.right = newTree
                  else:
                        return self.right.insert
      
      def getSmallestValue(self):
            if self.left == None:
                  return self.value
            return self.left.getSmallestValue()
      
      def getGreatestValue(self):
            if self.right == None:
                  return self.value
            return self.right.getGreatestValue()
      
      def listValues(self, order):
            values = []

            def traverse(node, order):
                  if order == 'in-order':
                        if node.left:
                              traverse(node.left, order)
                        values.append(node.value)
                        if node.right:
                              traverse(node.right, order)
                  if order == 'post-order':
                        if node.right:
                              traverse(node.right, order)
                        values.append(node.value)
                        if node.left:
                              traverse(node.left, order)

            traverse(self, order)
            return values



bst = BST(50)
bst.insert(44)
bst.insert(51)
bst.insert(46)
bst.insert(33)
print(bst.listValues('post-order'))