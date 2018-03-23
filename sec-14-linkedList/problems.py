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

print('17- cycleList: ', check_cycle(a))

def check_cycle_2(node):
      marker1 = node
      marker2 = node

      while marker2.next != None and marker2.next.next != None:
            marker1 = marker1.next
            marker2 = marker2.next.next

            if marker1 == marker2:
                  return True
      return False

print('18- cycleList 2 : ', check_cycle_2(a))

#=======================================================================================

# Reverse singly - linkedlist in place

'''
Given a singly LinkedList, write a function that revereses it in place

'''

a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)

a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5

def reverseList(node):

      prev_node = None

      while node != None:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node
      
      return node



print(reverseList(a1))
# print(a5.next.value)
