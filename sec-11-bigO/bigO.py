# O(1) constant
def func_constaant(values):
      return values[0]

lst = [1,2,3]
print(func_constaant(lst))

#----------------------------------
# O(n) Linear
def func_linear(lst):
      for val in lst:
            print(val)

print(func_linear(lst))

#----------------------------------
#O(n^2) Quadratic
def func_quadratic(lst):
      for val1 in lst:
            for val2 in lst:
                  print (val1, val2)

print(func_quadratic(lst))