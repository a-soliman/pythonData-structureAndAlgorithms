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



print('19- reverse Singly LinkedList: ', reverseList(a1))


#=======================================================================================

# nth to the last node

'''
Given a singly LinkedList head, and an integer value n,
return the nth to the last node in the linked list

'''

def nth_to_last(n, head):
      current = head
      nodes = []
      while current:
            nodes.append(current)
            current = current.next
      return nodes[-n]

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

print('20- nth_to_last_1: ', nth_to_last(1,a).value)


def nth_to_last_2(n, head):
      l = head
      r = head
      current = head

      # get the true r passed on n
      while current:
            n = n-1
            if n == 0:
                  r = current
                  break

            current = current.next
      
      while r:
            if r.next == None:
                  return l
            l = l.next
            r = r.next

print('22- nth_to_last_2: ', nth_to_last_2(2,a).value)  
