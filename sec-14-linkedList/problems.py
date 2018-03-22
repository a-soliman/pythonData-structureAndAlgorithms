'''
===============================================================================================================
================================================              =================================================
================================================|| PROBELMS ||=================================================
================================================              =================================================
===============================================================================================================
'''


#=======================================================================================

# Check cycle single linked list

'''
Given a singly LinkedList, write a function that determins if the linked list is cycle

'''

class Node(object):
      def __init__(self, value):
            self.value = value
            self.next = None

def check_cycle(node):
      
      nodes = []
      n = node

      while n.next:
            if n in nodes:
                  return True
            nodes.append(n)
            n = n.next
      return False

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a

print(check_cycle(a))