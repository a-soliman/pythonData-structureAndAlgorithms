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