import ctypes

class DynamicArray(object):
      
      def __init__(self):
            self.len          = 0
            self.capacity     = 1
            self.arr          = self.make_array(self.capacity)

      def _resize(self, new_cap):
            temp_arr = self.make_array(new_cap)

            for index in range(self.len):
                  temp_arr[index] = self.arr[index]
            
            self.arr = temp_arr
            self.capacity = new_cap
      
      def getitem(self, index):
            if index < 0 or index > self.len:
                  return IndexError('index is out of range!')
            
            return self.arr[index]

      def append(self, value):
            if self.len == self.capacity:
                  self._resize(2 * self.capacity)
            
            self.arr[self.len] = value
            self.len += 1

      def make_array(self, cap):
            return (cap * ctypes.py_object)()





#return (cap * ctypes.py_object)()