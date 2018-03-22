# implement a doubly linked list class with clear, size, isEmpty, getValues, addToHead, addToTail, removeHead, remvoeTail, contains, getIndex, insertAtIndex

class Node(object):
      def __init__(self, value):
            self.value = value
            self.prev = None
            self.next = None

class LinkedList(object):
      def __init__(self):
            self.head = None
            self.tail = None
            self.items = []

      def clear(self):
                  self.head = self.tail = None
                  self.items = []

      def size(self):
            return len(self.items)

      def isEmpty(self):
            return self.size() == 0

      def getValues(self):
            values = []

            for item in self.items:
                  values.append(item.value)
            
            return values

      def addToHead(self, value):
            newNode = Node(value)

            if not self.head:
                  self.tail = newNode
            else:
                  self.head.prev = newNode
                  newNode.next = self.head

            self.items.insert(0, newNode)
            self.head = newNode

      def addToTail(self, value):
            newNode = Node(value)

            if not self.tail:
                  self.head = newNode
            else:
                  self.tail.next = newNode
                  newNode.prev = self.tail
            
            self.items.append(newNode)
            self.tail = newNode
      
      def removeHead(self):
            if self.size() == 0:
                  return False
            if self.size() == 1:
                  value = self.head.value
                  self.clear()
                  return value
            
            if self.size() == 2:
                  value = self.head.value
                  self.tail.prev = None
                  self.head = self.tail
                  self.items.pop(0)
                  return value
            
            old_head = self.head
            self.head = self.head.next
            self.head.prev = None
            self.items.pop(0)
            return old_head.value