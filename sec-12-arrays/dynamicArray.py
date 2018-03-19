import ctypes

class DynamicArray(object):
      
      def __init__(self):
            self.len          = 0
            self.capacity     = 1
            self.arr          = self.make_array(self.capacity)

      



#return (cap * ctypes.py_object)()