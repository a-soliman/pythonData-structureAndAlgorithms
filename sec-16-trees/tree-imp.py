class Tree(object):
      def __init__(self, value):
            self.value = value
            self.children = []
      
      def _append(self, value):
            if value == 'head' or value == 'body':
                  new_tree = Tree(value)
                  self.children.append(new_tree)
      
      def insert(self, value):
            if value == 'title' or value == 'meta' or value == 'link':
                  if self.value == 'head':
                        new_tree = Tree(value)
                        self.children.append(new_tree)
                        return
                  else:
                        #create head and append to it
                        self._append('head')
                        index = self.getIndexOfChild('head')
                        return self.children[index].insert(value)

            elif value == 'head' or value == 'body' :
                  return self._append(value)

            else:
                  if self.value == 'body':
                        #append to body
                        new_tree = Tree(value)
                        self.children.append(new_tree)
                        return
                  else:
                        #create body and append to it
                        self._append('body')
                        index = self.getIndexOfChild('body')
                        return self.children[index].insert(value)

      
      def listChildren(self):
            children = [i.value for i in self.children]
            return children

      def getIndexOfChild(self, value):
            if not value in self.listChildren():
                  return False
            
            for i in range(0, len(self.children)):
                  if self.children[i].value == value:
                        return i




t = Tree('Html')
t.insert('title')
t.insert('h1')
print(t.listChildren())
