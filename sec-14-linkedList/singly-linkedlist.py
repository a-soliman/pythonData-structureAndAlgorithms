from snode import Node

class LinkedList(object):
      def __init__(self):
            self.head = None
            self.tail = None
            self.items = []

      def addToHead(self, value):
            newNode = Node(value)

            if not self.head:
                  self.tail = newNode
            else:
                  newNode.next = self.head
                  
            self.items.insert(0, newNode)
            self.head = newNode
      
      def addToTail(self, value):
            newNode = Node(value)

            if not self.tail:
                  self.head = newNode
            else:
                  self.tail.next = newNode
            
            self.items.append(newNode)
            self.tail = newNode

      def removeHead(self):
            if not self.head:
                  return False
            
            if self.head == self.tail:
                  self.head = self.tail = None
                  self.items = []
            else:
                  oldHead = self.head
                  self.head = self.head.next
                  oldHead.next = None
                  self.items.pop(0)

      def removeTail(self):
            if not self.tail:
                  return False
            
            if self.tail == self.head:
                  self.tail = self.head = None
                  self.items = []
            
            else:
                  self.items.pop()
                  newTail = self.items[len(self.items)-1]
                  newTail.next = None
                  self.tail = newTail

      def getValues(self):
            values = [ n.value for n in self.items ]
            return values



'''
===============================================================================================================
================================================              =================================================
================================================|| PROBELMS ||=================================================
================================================              =================================================
===============================================================================================================
'''