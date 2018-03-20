# implement a stack

class Stack(object):

      def __init__(self):
            self.items = []

      def push(self, item):
            self.items.append(item)

      def pop(self):
            item = self.items.pop()
            return item

      def peek(self):
            return self.items[len(self.items)-1]
      
      def isEmpty(self):
            return len(self.items) == 0
      
      def size(self):
            return len(self.items)


stack = Stack()
stack.push('Hello')
stack.push('Hey')
# print(stack.pop())
print(stack.peek())
print('* isEmpty(): ', stack.isEmpty())
print('* size(): ', stack.size())
