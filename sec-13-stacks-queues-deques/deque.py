# implement a Deque class
class Deque(object):
      def __init__(self):
            self.items = []
      
      def isEmpty(self):
            return len(self.items) == 0
      def size(self):
            return len(self.items)
            
      def addFront(self, item):
            self.items.insert(0,item)
      
      def addRear(self, item):
            self.items.append(item)

      def removeFront(self):
            if self.isEmpty() == True:
                  return 
            item = self.items.pop(0)
            return item

      def removeRear(self):
            if self.isEmpty() == True:
                  return 
            item = self.items.pop()
            return item

d = Deque()

print('isEmpty(): ', d.isEmpty())
print('size(): ', d.size())
d.addFront(4)
d.addFront(6)
d.addFront(5)
print(d.removeFront())


d.addRear(1)
d.addRear(2)
d.addRear(3)
print(d.removeRear())
print(d.items)
print('isEmpty(): ', d.isEmpty())
print('size(): ', d.size())