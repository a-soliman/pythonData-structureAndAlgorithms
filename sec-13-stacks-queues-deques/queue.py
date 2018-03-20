# implement a Queue
class Queue(object):
      def __init__(self):
            self.items = []

      def enqueue(self, item):
            self.items.append(item)

      def dequeue(self):
            item = self.items.pop(0)
            return item

      def isEmpty(self):
            return len(self.items) == 0

      def size(self):
            return len(self.items)


q = Queue()
q.enqueue('20')
q.enqueue('23')
print(q.items)
print(q.dequeue())
print('size(): ', q.size())
print('isEmpty(): ', q.isEmpty())

