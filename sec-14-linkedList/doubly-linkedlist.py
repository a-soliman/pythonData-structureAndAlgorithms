# implement a doubly linked list class with clear, size, isEmpty, getValues, addToHead, addToTail, removeHead, remvoeTail, contains, getIndex, insertAtIndex
from dnode import Node


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

      def removeTail(self):
            if self.size() == 0:
                  return False
            
            if self.size() == 1:
                  value = self.tail.value
                  self.clear()
                  return value
            
            if self.size() == 2:
                   value = self.tail.value
                   self.tail = self.head
                   self.head.next = None
                   self.items.pop()
                   return value
            
            old_tail = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.items.pop()
            return old_tail.value

      def contains(self, value):
            if self.size() > 0:
                  for item in self.items:
                        if item.value == value:
                              return True
            return False

      def getIndex(self, value):
            if not self.contains(value):
                  return False
            for index in range(len(self.items)):
                  if self.items[index].value == value:
                        return index

      def insertAtIndex(self, index, value):
            if index > len(self.items) -1:
                  return False

            if index == 0:
                  return self.addToHead(value)

            if index == len(self.items) -1:
                  return self.addToTail(value)

            new_node = Node(value)
            before_node = self.items[index-1]
            after_node = self.items[index]

            before_node.next = new_node
            new_node.prev = before_node

            after_node.prev = new_node
            new_node.next = after_node

            self.items.insert(index, new_node)


'''
===============================================================================================================
================================================              =================================================
================================================|| PROBELMS ||=================================================
================================================              =================================================
===============================================================================================================
'''