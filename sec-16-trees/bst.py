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
      