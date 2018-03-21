#=======================================================================================

# Balanced Prentheses

'''
Given a string of opening and closing parentheses, check whether it's balanced.
Assume that the string doesn't contain words or numbers, and you can assume that the string has no spaces


EX:
      '([])'
      output True
EX:
      '([)]'
      output: False
'''

def balance_check(string):
      if len(string) == 0:
            return 
      openining = ('(', '{', '[')
      matches = set([ ('(', ')'), ('[', ']'), ('{', '}') ])
      stack =[]

      for char in string:
            if char in openining:
                  stack.append(char)
            else:
                  for o,c in matches:
                        if c == char:
                              if o != stack.pop():
                                    return False
      return True
                                    
      
print('13- balance_check: ', balance_check('([[]])'))

#=======================================================================================

# Queue out of two stacks

'''
given two stacks, implement your own queue

'''

class QueueOfTwoStacks(object):
      def __init__(self):
            self.inStack = []
            self.outStack = []
      
      def inqueue(self, item):
            self.inStack.append(item)
      
      def dequeue(self):
            if not self.outStack:
                  while self.inStack:
                        self.outStack.append(self.inStack.pop())
            
            return self.outStack.pop()
      

q = QueueOfTwoStacks()
for i in range(0, 5):
      q.inqueue(i)

for j in range(0,5):
      print(q.dequeue())